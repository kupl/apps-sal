s = int(input())

ans = 0
dp = [1, 0, 0]

if s ==1 or s == 2:
    ans = 0
else:
    for i in range(3, s+1):
        dpi = 0
        for j in range(i-2):
            dpi += dp[j]
            dpi = dpi % ((10**9) + 7)
        dp.append(dpi)
print(dp[s])
