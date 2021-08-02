n, k, *a = list(map(int, open(0).read().split()))

ans = 0
for l in range(0, k + 1):
    for r in range(0, k + 1 - l):
        if l == r == 0 or l + r > n:
            continue
        b = sorted(a[:l] + a[n - r:])
        c = min(k - l - r, len(b) - 1)
        ans = max(ans, sum(b[c:] if b[c] < 0 else [x for x in b if x > 0]))
print(ans)
