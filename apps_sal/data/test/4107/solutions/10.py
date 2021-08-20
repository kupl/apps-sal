(n, k) = map(int, input().split())
s = input()
inf = 10 ** 18
who = [-1] * n
for i in range(n):
    if s[i] == '1':
        for j in range(min(n - 1, i + k), i - 1, -1):
            if who[j] == -1:
                who[j] = i
            else:
                break
for i in range(n):
    if s[i] == '1':
        for j in range(i - 1, max(-1, i - k - 1), -1):
            if who[j] == -1:
                who[j] = i
            else:
                break
dp = [inf] * (n + 1)
dp[n] = 0
for i in range(n, 0, -1):
    dp[i - 1] = min(dp[i - 1], dp[i] + i)
    if who[i - 1] != -1:
        dp[max(0, who[i - 1] - k)] = min(dp[max(0, who[i - 1] - k)], dp[i] + who[i - 1] + 1)
print(dp[0])
