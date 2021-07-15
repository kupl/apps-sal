n = int(input())
dp = [0] + [n] * n + [0]
a = tuple(map(int, input().split()))
s = [1]
dp[1] = 0
while s:
    ns = []
    for v in s:
        if dp[v - 1] == n:
            ns.append(v - 1)
        dp[v - 1] = min(dp[v - 1], dp[v] + 1)
        if dp[v + 1] == n:
            ns.append(v + 1)
        dp[v + 1] = min(dp[v + 1], dp[v] + 1)
        if dp[a[v - 1]] == n:
            ns.append(a[v - 1])
        dp[a[v - 1]] = min(dp[a[v - 1]], dp[v] + 1)
    s = ns
print(' '.join(map(str, dp[1:-1])))

