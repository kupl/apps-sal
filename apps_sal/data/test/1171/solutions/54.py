n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
for l in range(0, k + 1):
    for r in range(0, k + 1 - l):
        if l == r == 0 or l + r > n:
            continue
        a = sorted(v[:l] + v[n - r:])
        m = min(k - l - r, len(a) - 1)
        ans = max(ans, sum(a[m:] if a[m] <
                           0 else filter(lambda x: x > 0, a)))
print(ans)
