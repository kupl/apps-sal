def solve(n: int) -> int:
    mod = 1e9 + 7
    n_bin = '0' + bin(n)[2:]

    dp = [[0, 0, 0] for _ in range(len(n_bin))]
    dp[-1][0] = 1
    for i in range(len(n_bin) - 2, -1, -1):
        for s in range(3):
            for k in range(3):
                s2 = min(2, 2 * s + int(n_bin[len(n_bin) - i - 1]) - k)
                if s2 >= 0:
                    dp[i][s2] = int((dp[i][s2] + dp[i + 1][s]) % mod)

    return int(sum(dp[0]) % mod)

n = int(input())
print(solve(n))
