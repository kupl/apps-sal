n, h, k = map(int, input().split())
a = list(map(int, input().split()))
h1 = 0
ans = 0
i = 0
while i < n:
    while i < n and h1 + a[i] <= h:
        h1 += a[i]
        i += 1
    if h1 < k:
        ans += 1
        h1 = 0
    ans += h1 // k
    h1 %= k
if (h1 != 0):
    ans += 1
print(ans)
