(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
l = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1 ** 10] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(m):
        if i >= l[a[j]] and dp[i] < dp[i - l[a[j]]] + 1:
            dp[i] = dp[i - l[a[j]]] + 1
ans = []
remain = dp[-1]
now = n
for i in a:
    x = l[i]
    while now - x >= 0 and dp[now] == dp[now - x] + 1:
        ans.append(i)
        now -= x
print(*ans, sep='')
