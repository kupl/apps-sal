import os
import sys
import numpy as np


def solve(N, U, V, AB):
    G = [[0] * 0 for _ in range(N + 1)]
    for idx_ab in range(len(AB)):
        a, b = AB[idx_ab]
        G[a].append(b)
        G[b].append(a)
    P1 = np.zeros(N + 1, dtype=np.int64)

    def dfs1(u):
        st = [u]
        while st:
            v = st.pop()
            p = P1[v]
            for u in G[v]:
                if p != u:
                    st.append(u)
                    P1[u] = v
    dfs1(U)
    path_u2v = [U]
    v = V
    while v != U:
        v = P1[v]
        path_u2v.append(v)
    path_u2v.reverse()
    l = len(path_u2v)
    half = (l - 2) // 2
    c = path_u2v[half]
    ng = path_u2v[half + 1]
    Depth = np.zeros(N + 1, dtype=np.int64)

    def dfs2(c):
        st = [c]
        P = np.zeros(N + 1, dtype=np.int64)
        while st:
            v = st.pop()
            p = P[v]
            d = Depth[v]
            for u in G[v]:
                if p != u and u != ng:
                    st.append(u)
                    P[u] = v
                    Depth[u] = d + 1
    dfs2(c)
    c_ = path_u2v[l - 1 - half]
    v = c_
    while v != c:
        Depth[v] = 0
        v = P1[v]
    d = l % 2
    ans = max(Depth) + half + d
    return ans


# >>> numba compile >>>
numba_config = [
    [solve, "i8(i8,i8,i8,i8[:,:])"],
]
if sys.argv[-1] == "ONLINE_JUDGE":
    from numba import njit
    from numba.pycc import CC
    cc = CC("my_module")
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature)(func)
        cc.export(func.__name__, signature)(func)
    cc.compile()
    return
elif os.name == "posix":
    exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
else:
    from numba import njit
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature, cache=True)(func)
    print("compiled!", file=sys.stderr)
# <<< numba compile <<<


def main():
    N, u, v = map(int, input().split())
    if N == 2:
        print(0)
        return
    AB = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(N - 1, 2)
    ans = solve(N, u, v, AB)
    print(ans)


main()
