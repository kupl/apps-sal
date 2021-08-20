(n, m) = map(int, input().split())
dp = [float('inf') for i in range(1 << n)]
dp[0] = 0
for i in range(m):
    (a, b) = map(int, input().split())
    c = list(map(int, input().split()))
    bit = 0
    for j in range(b):
        bit |= 1 << c[j] - 1
    for j in range(1 << n):
        dp[j | bit] = min(dp[j | bit], dp[j] + a)
if dp[-1] == float('inf'):
    print('-1')
else:
    print(dp[-1])
