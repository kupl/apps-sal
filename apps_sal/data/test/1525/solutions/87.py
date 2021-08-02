import sys
input = sys.stdin.readline
INF = 10**9
MOD = 10**9 + 7


def main():
    h, w, k = list(map(int, input().split()))

    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1

    for i in range(h):
        for bit in range(1 << (w - 1)):
            flag = False
            before = -2
            line = [0] * (w - 1)
            for j in range(w - 1):
                if (bit >> j) & 1:
                    if before + 1 == j:
                        flag = True
                        break

                    else:
                        before = j
                        line[j] = 1

            if flag:
                continue

            j = 0
            while j < w:
                if j == w - 1:
                    dp[i + 1][j] += dp[i][j]
                    dp[i + 1][j] %= MOD
                    break
                if line[j]:
                    dp[i + 1][j] += dp[i][j + 1]
                    dp[i + 1][j] %= MOD
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= MOD
                    j += 2
                else:
                    dp[i + 1][j] += dp[i][j]
                    dp[i + 1][j] %= MOD
                    j += 1

    print((dp[-1][k - 1] % MOD))


def __starting_point():
    main()


__starting_point()
