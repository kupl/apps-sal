import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *ABC = list(map(int, read().split()))
    G = [[INF] * N for _ in range(N)]
    edge = [0] * M
    for i, (a, b, c) in enumerate(zip(*[iter(ABC)] * 3)):
        edge[i] = (a - 1, b - 1, c)
        G[a - 1][b - 1] = G[b - 1][a - 1] = c
    for i in range(N):
        G[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]

    ans = 0
    for a, b, c in edge:
        used = False
        for i in range(N):
            if G[i][b] == G[i][a] + c or G[i][a] == G[i][b] + c:
                used = True
                break
        if not used:
            ans += 1

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
