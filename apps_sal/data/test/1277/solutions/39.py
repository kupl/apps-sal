import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)


def input():
    return sys.stdin.readline().strip()


'\nPypyは再帰が遅いらしいのでPythonで通してみる\n'


def main():
    (N, u, v) = list(map(int, input().split()))
    u -= 1
    v -= 1
    repn = [[] for _ in range(N)]
    for i in range(N - 1):
        (a, b) = list(map(int, input().split()))
        repn[a - 1].append((b - 1, i))
        repn[b - 1].append((a - 1, i))
    '\n    まずu, vを結ぶ単純パス上にあるnodeを列挙する。\n    これはvを根とする根付き木に対するdfs（再帰）により求まる（参考：ABC152F）\n    '
    path = []

    def connected(v, tv, p=-1):
        if v == tv:
            return True
        for (w, _) in repn[v]:
            if w == p:
                continue
            elif connected(w, tv, v):
                path.append(w)
                return True
        return False
    connected(v, u)
    path.append(v)
    '\n    次にu, vを結ぶ単純パスP上の各頂点wに対して、wからPに沿わない向きにどれだけ深く潜れるかを求める。\n    しかし最終的には「頂点vから（高橋君が逃げ込める中で）最も遠い頂点」を求めればよいので、\n    uvの中点からdfsすれば十分。\n    '

    def dfs(v, p):
        d = -1
        for (w, _) in repn[v]:
            if w == p:
                continue
            else:
                d = max(d, dfs(w, v))
        return d + 1
    dist = len(path)
    mid = path[dist // 2 - 1]
    par = path[dist // 2]
    ans = dfs(mid, par)
    print(ans + (dist - 1) // 2)


def __starting_point():
    main()


__starting_point()
