import sys
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson, csgraph_from_dense
import itertools

input = sys.stdin.readline


def main():
    N, M, R = [int(x) for x in input().split()]
    r = [int(x) - 1 for x in input().split()]
    ABC = [[int(x) for x in input().split()] for _ in range(M)]

    EDGE = [[10 ** 9] * N for j in range(N)]

    for a, b, c in ABC:
        EDGE[a - 1][b - 1] = c
        EDGE[b - 1][a - 1] = c

    G = csgraph_from_dense(EDGE, null_value=10 ** 9)

    d = floyd_warshall(G)

    ans = float("inf")
    for a in itertools.permutations(r):
        tmp = 0
        c = a[0]
        for n in a:
            tmp += int(d[c][n])
            c = n
        ans = min(ans, tmp)

    print(ans)


def __starting_point():
    main()


__starting_point()
