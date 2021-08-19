import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, K) = list(map(int, readline().split()))
    point = list(map(int, readline().split()))
    T = readline().strip()
    T = list(map(int, T.translate(str.maketrans('rsp', '012'))))
    ans = 0
    for i in range(K):
        M = (N - i + K - 1) // K
        dp = [[0] * 3 for _ in range(M + 1)]
        for j in range(M):
            for k in range(3):
                dp[j + 1][k] = max(dp[j][(k + 1) % 3], dp[j][(k + 2) % 3])
                if (k + 1) % 3 == T[i + j * K]:
                    dp[j + 1][k] += point[k]
        ans += max(dp[M])
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
