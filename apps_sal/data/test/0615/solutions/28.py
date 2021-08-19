n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    a[i + 1] += a[i]
l = 0
r = 2
ans = float('inf')
for m in range(1, n - 1):
    while abs(2 * a[l] - a[m]) > abs(2 * a[l + 1] - a[m]):
        l += 1
    while abs(2 * a[r] - a[n - 1] - a[m]) > abs(2 * a[r + 1] - a[n - 1] - a[m]):
        r += 1
    bcde = [a[l], a[m] - a[l], a[r] - a[m], a[n - 1] - a[r]]
    ans = min(ans, max(bcde) - min(bcde))
print(ans)
