from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
L = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
D = defaultdict(int)

for i in A:
    if D[L[i]] < i:
        D[L[i]] = i

INF = float("inf")
dp = [-INF] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for j in D.keys():
        if i - j >= 0:
            dp[i] = max(dp[i], dp[i - j] + 1)
        else:
            dp[i] = max(dp[i], -INF)

ans = ""
temp = N

while temp > 0:
    for i, x in sorted(D.items(), key=lambda x: x[1], reverse=True):
        if temp - i >= 0 and dp[temp - i] == dp[temp] - 1:
            ans += str(x)
            temp -= i
            break

print(ans)
