n, m = list(map(int, input().split()))
can_open = []
cost = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    cost.append(a)
    can_open.append(sum(1 << (c - 1) for c in map(int, input().split())))

n_bit = 1 << n
INF = 10**18
dp = [INF] * n_bit
dp[0] = 0

for x, y in zip(can_open, cost):
    for j in range(n_bit):
        m = j | x
        z = dp[j] + y
        if dp[m] > z:
            dp[m] = z

print((dp[-1] if dp[-1] != INF else -1))
