import sys
from itertools import permutations

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, R = list(map(int, readline().split()))
    city = [int(s) - 1 for s in readline().split()]
    ABC = list(map(int, read().split()))

    G = [[INF] * N for _ in range(N)]
    for a, b, c in zip(*[iter(ABC)] * 3):
        G[a - 1][b - 1] = G[b - 1][a - 1] = c

    for i in range(N):
        G[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]

    ans = INF
    for plan in permutations(city):
        res = 0
        for i in range(R - 1):
            res += G[plan[i]][plan[i + 1]]
        if ans > res:
            ans = res

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
