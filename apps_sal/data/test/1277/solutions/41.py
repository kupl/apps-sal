import os
import sys
import numpy as np

def solve(N, U, V, AB):
    G = [[] for _ in range(N+1)]
    for ab in AB:
        a, b = ab
        G[a].append(b)
        G[b].append(a)
    P1 = np.zeros(N+1, dtype=np.int64)
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
    half = (l-2) // 2
    c = path_u2v[half]
    ng = path_u2v[half+1]
    Depth = np.zeros(N+1, dtype=np.int64)
    def dfs2(c):
        st = [c]
        P = np.zeros(N+1, dtype=np.int64)
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
    c_ = path_u2v[l-1-half]
    v = c_
    while v != c:
        Depth[v] = 0
        v = P1[v]
    d = l%2
    ans = max(Depth) + half + d
    return ans

def main():
    N, u, v = list(map(int, input().split()))
    if N==2:
        print((0))
        return
    AB = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(N-1, 2)
    ans = solve(N, u, v, AB)
    print(ans)

main()

