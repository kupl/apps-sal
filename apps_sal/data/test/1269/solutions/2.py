def main():
    line = input().split()
    n = int(line[0])
    line = input().split()
    v = [int(x) for x in line]
    mod = 998244353
    dp = [[1] * (n + 5) for i in range(n + 5)]
    for sz in range(2, n + 1):
        for lo in range(1, n - sz + 2):
            hi = lo + sz - 1
            (pos, num) = (-1, n + 5)
            for k in range(lo, hi + 1):
                if v[k - 1] < num:
                    num = v[k - 1]
                    pos = k
            (s1, s2) = (0, 0)
            for k in range(lo, pos + 1):
                cnt = dp[lo][k - 1] * dp[k][pos - 1] % mod
                s1 = (s1 + cnt) % mod
            for k in range(pos, hi + 1):
                cnt = dp[pos + 1][k] * dp[k + 1][hi] % mod
                s2 = (s2 + cnt) % mod
            dp[lo][hi] = s1 * s2 % mod
    print(dp[1][n])


main()
