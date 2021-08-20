(n, m) = list(map(int, input().split()))
kagi = [[] for _ in range(m)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    X = list(map(int, input().split()))
    bit = 0
    for x in X:
        bit |= 2 ** (x - 1)
    kagi[i] = [a, bit]
ok = 2 ** n - 1
kagi.sort(key=lambda x: x[1])
zenkai = 2 ** n
dp = [float('inf')] * int(zenkai + 1)
dp[0] = 0
for i in range(2 ** n):
    if dp[i] == float('inf'):
        continue
    for j in range(m):
        s = i | kagi[j][1]
        dp[s] = min(dp[s], dp[i] + kagi[j][0])
if dp[zenkai - 1] == float('inf'):
    print(-1)
else:
    print(dp[zenkai - 1])
