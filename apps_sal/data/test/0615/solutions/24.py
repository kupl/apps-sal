n = int(input())
a = list(map(int, input().split()))

s = [a[0]]
for i in range(1, n):
    s.append(a[i] + s[i - 1])

l = 0
r = 2
ans = float("inf")

for m in range(1, n - 1):
    while l < m - 1 and abs(s[m] - 2 * s[l]) > abs(s[m] - 2 * s[l + 1]):
        l += 1
    while r <= m or r < n - 1 and abs(s[n - 1] - 2 * s[r] + s[m]) > abs(s[n - 1] - 2 * s[r + 1] + s[m]):
        r += 1
    mx = max(s[l], s[m] - s[l], s[r] - s[m], s[n - 1] - s[r])
    mn = min(s[l], s[m] - s[l], s[r] - s[m], s[n - 1] - s[r])
    ans = min(ans, mx - mn)

print(ans)
