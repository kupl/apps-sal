n = int(input())
cake = list(map(int, input().split()))
cake.reverse()
pref = [0]
for i in range(n):
    pref.append(cake[i] + pref[-1])
dp = [0] * n
dp[0] = cake[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1], cake[i] + pref[i] - dp[i - 1])
print(pref[n] - dp[n - 1], dp[n - 1])
