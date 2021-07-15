import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
bin_k = bin(K)[2:].zfill(50)
cnt = [0] * 50

for a in A:
    bin_a = bin(a)[2:]
    for i, b in enumerate(bin_a[::-1]):
        if b == "1":
            cnt[i] += 1

cnt = cnt[::-1]
dp = [[0] * 2 for _ in range(50 + 1)]
ans = 0
base = 2 ** (50 - 1)
flag = False

for i, c in enumerate(cnt, 1):
    if flag:
        if bin_k[i - 1] == "1":
            dp[i][0] = dp[i - 1][0] + base * (N - c)
            dp[i][1] = max(dp[i - 1][0] + base * c, dp[i - 1][1] + base * c,
                        dp[i - 1][1] + base * (N - c))
        else:
            dp[i][0] = dp[i - 1][0] + base * c
            dp[i][1] = max(dp[i - 1][1] + base * c, dp[i - 1][1] + base * (N - c))
    else:
        if bin_k[i - 1] == "1":
            dp[i][0] = dp[i - 1][0] + base * (N - c)
            tmp1 = dp[i - 1][0] + base * c
            tmp2 =  dp[i - 1][1] + base * c
            tmp3 = dp[i - 1][1] + base * (N - c)
            if tmp3 <= tmp1 and tmp3 <= tmp2:
                dp[i][1] = max(tmp1, tmp2)
                flag = True
            elif tmp3 <= tmp1:
                dp[i][1] = tmp1
                flag = True
            else:
                dp[i][1] = tmp3
        else:
            dp[i][0] = dp[i - 1][0] + base * c
            dp[i][1] = dp[i - 1][1] + base * c

    base //= 2

print(max(dp[50][0], dp[50][1]))
