n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
s, r = 0, 0
for l in range(n):
    while (r < n) and (s + a[r] <= t):
        s += a[r]
        r += 1
    ans = max(ans, r - l)
    s -= a[l]
print(ans)
