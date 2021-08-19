import heapq
import sys
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    (N, M) = list(map(int, input().split()))
    dp = [[float('inf')] * N for _ in range(N)]
    edges = list()
    for i in range(N):
        dp[i][i] = 0
    for _ in range(M):
        (a, b, c) = list(map(int, input().split()))
        a -= 1
        b -= 1
        dp[a][b] = c
        dp[b][a] = c
        if a > b:
            (a, b) = (b, a)
        edges.append((a, b, c))
    for k in range(N):
        for i in range(N):
            for j in range(N):
                tmp = dp[i][k] + dp[k][j]
                if tmp < dp[i][j]:
                    dp[i][j] = tmp
    ans = 0
    for (i, j, c) in edges:
        if dp[i][j] < c:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
