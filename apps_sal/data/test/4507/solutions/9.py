n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a)
a = a[:k]
d = [(1, 0)]
for i in range(m):
    x, y = list(map(int, input().split()))
    if x > k:
        continue
    d.append((x, y))
d = sorted(d)

s = [0] * (k + 1)
s[1] = a[0]
for i in range(1, k + 1):
    s[i] = s[i - 1] + a[i - 1]
INF = float('inf')
dp = [INF] * (k + 1)
dp[0] = 0
for i in range(k + 1):
    for j in range(len(d)):
        x, y = d[j]
        if i + x <= k:
            dp[i + x] = min(dp[i + x], dp[i] + s[i + x] - s[i + y])
        else:
            break

print(dp[k])


