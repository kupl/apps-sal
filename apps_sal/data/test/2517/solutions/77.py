from sys import stdin
from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import csgraph_from_dense


def main():
    readline = stdin.readline
    inf = 10 ** 9
    (n, m, r) = map(int, readline().split())
    targets = list(map(lambda x: int(x) - 1, readline().split()))
    G = [[inf] * n for _ in range(n)]
    for _ in range(m):
        (a, b, c) = map(int, readline().split())
        a -= 1
        b -= 1
        G[a][b] = min(G[a][b], c)
        G[b][a] = min(G[b][a], c)
    G = csgraph_from_dense(G, null_value=10 ** 9)
    li = floyd_warshall(G)
    li = [list(map(int, li[i])) for i in range(n)]
    ans = inf
    for p in permutations(targets, r):
        tmp = 0
        for i in range(r - 1):
            now = p[i]
            nex = p[i + 1]
            tmp += li[now][nex]
        ans = min(ans, tmp)
    print(ans)


def __starting_point():
    main()


__starting_point()
