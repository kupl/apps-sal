(H, W, K) = map(int, input().split())
mod = 10 ** 9 + 7
dp = [0] * W
dp[0] = 1
OK = [0, 1, 1, 2, 3, 5, 8, 13]
NG = [0, 1, 2, 3, 5, 8, 13, 21]
if W == 1:
    print(dp[K - 1])
else:
    for _ in range(H):
        temp = dp[:]
        for i in range(W):
            if i == 0:
                dp[i] = temp[i] * NG[W - 1 - i] + temp[i + 1] * OK[W - 1 - i]
            elif i == W - 1:
                dp[i] = temp[i - 1] * OK[i] + temp[i] * NG[i]
            else:
                dp[i] = temp[i - 1] * OK[i] * NG[W - 1 - i] + temp[i] * NG[i] * NG[W - 1 - i] + temp[i + 1] * NG[i] * OK[W - 1 - i]
            dp[i] %= mod
    print(dp[K - 1])
