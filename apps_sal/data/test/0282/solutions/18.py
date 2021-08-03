n, d = map(int, input().split())
a = [1000] * (n + 1)
a[0] = 0
s = [int(x) for x in input()]
for x in range(1, n):
    if s[x]:
        for c in range(1, d + 1):
            if x - c >= 0 and s[x - c]:
                a[x] = min(a[x - c] + 1, a[x])
print(-1 if a[n - 1] > 200 else a[n - 1])
