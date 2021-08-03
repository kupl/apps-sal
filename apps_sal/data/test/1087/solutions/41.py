n, k = map(int, input().split())
A = list(map(int, input().split()))

k_bin = "{:040b}".format(k)
A_bin = list(map(lambda x: '{:040b}'.format(x), A))
dp = [[0] * 2 for _ in range(41)]
for i, col in enumerate(zip(*A_bin)):
    zero_cnt = col.count('0')
    one_cnt = n - zero_cnt

    p = 40 - i - 1

    if dp[i][0] != 0:
        dp[i + 1][0] = dp[i][0] + max(zero_cnt, one_cnt) * 2**p

    if k_bin[i] == '0':
        dp[i + 1][1] = dp[i][1] + one_cnt * 2**p
    else:
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][1] + one_cnt * 2**p)
        dp[i + 1][1] = dp[i][1] + zero_cnt * 2**p

print(max(dp[-1]))
