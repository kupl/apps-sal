n = int(input())
k = input().strip()
power = [1]
for i in range(20):
    power.append(power[-1] * 10)
dp = [10 ** 18] * len(k)
for i in range(len(k)):
    for j in range(min(10, i + 1)):
        if k[i - j] == '0' and j > 0:
            continue
        s = int(k[i - j:i + 1])
        if s >= n:
            break
        if i - j > 0:
            dp[i] = min(dp[i], dp[i - j - 1] * n + s)
        else:
            dp[i] = min(dp[i], s)
print(dp[len(k) - 1])
