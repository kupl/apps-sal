h, w, k = list(map(int, input().split()))
mod = 10**9 + 7

if w == 1:
    print((1))
    return

dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
for i in range(1, h + 1):
    for p in range(2**(w - 1)):
        L = [0] * (w - 1)
        for q in range(w - 1):
            if (p >> q) & 1:
                L[q] = 1
        flag = True
        for q in range(w - 2):
            if L[q] == 1 and L[q + 1] == 1:
                flag = False
        if not flag:
            continue
        for j in range(w):
            if j == 0:
                if L[j] == 1:
                    dp[i][j] += dp[i - 1][1]
                else:
                    dp[i][j] += dp[i - 1][0]
            elif j == w - 1:
                if L[j - 1] == 1:
                    dp[i][j] += dp[i - 1][w - 2]
                else:
                    dp[i][j] += dp[i - 1][w - 1]
            else:
                if L[j - 1] == 1:
                    dp[i][j] += dp[i - 1][j - 1]
                elif L[j] == 1:
                    dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] += dp[i - 1][j]
            dp[i][j] %= mod

# print(dp)
print((dp[h][k - 1]))
