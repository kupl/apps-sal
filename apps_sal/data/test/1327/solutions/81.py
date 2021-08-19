(n, m) = list(map(int, input().split()))
xyz = [list(map(int, input().split())) for _ in range(n)]
inf = float('inf')
ans = -inf


def func(multi):
    dp = [-inf] * (m + 1)
    dp[0] = 0
    for i in range(n):
        (x, y, z) = xyz[i]
        for j in range(min(i + 1, m), 0, -1):
            dp[j] = max(dp[j], dp[j - 1] + x * multi[0] + y * multi[1] + z * multi[2])
    return dp[m]


for i in range(8):
    multi = [1] * 3
    for j in range(3):
        if i >> j & 1:
            multi[j] = -1
    ans = max(ans, func(multi))
print(ans)
