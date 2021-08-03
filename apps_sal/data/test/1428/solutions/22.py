import sys
from itertools import permutations

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, C = list(map(int, readline().split()))
    D = [0] * C
    for i in range(C):
        D[i] = list(map(int, readline().split()))
    G = [0] * N
    for i in range(N):
        G[i] = [int(s) - 1 for s in readline().split()]

    cost = [[0] * C for _ in range(3)]
    for x in range(N):
        for y in range(N):
            color = G[x][y]
            cost_current = cost[(x + y) % 3]
            for i in range(C):
                cost_current[i] += D[color][i]

    ans = INF
    for c1, c2, c3 in permutations(list(range(C)), 3):
        if ans > cost[0][c1] + cost[1][c2] + cost[2][c3]:
            ans = cost[0][c1] + cost[1][c2] + cost[2][c3]

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
