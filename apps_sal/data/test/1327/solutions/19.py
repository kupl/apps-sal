from itertools import product
n, m = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(n)]


ans = 0
for subset in product((-1, 1), repeat=3):
    INF = 10**18
    dp = [-INF]*(n+1)
    dp[0] = 0

    def func(xyz):
        return sum(x*a for x, a in zip(xyz, subset))

    values = list(map(func, xyz))
    for i, val in enumerate(values, 1):
        for j in reversed(range(1, i+1)):
            dp[j] = max(dp[j-1]+val, dp[j])
    if ans < dp[m]:
        ans = dp[m]

print(ans)
