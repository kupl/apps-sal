INF = 10 ** 6
(n, m) = list(map(int, input().split()))
dp = [INF] * 2 ** n
dp[0] = 0
for i in range(m):
    (a, b) = list(map(int, input().split()))
    bit = ['0'] * n
    for x in set(map(int, input().split())):
        bit[x - 1] = '1'
    bit = int(''.join(bit), 2)
    for j in range(2 ** n - 1, -1, -1):
        dp[j | bit] = min(dp[j | bit], a + dp[j])
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
