n, w = map(int, input().split())
maxp, minp = 0, 0
a = list(map(int, input().split()))
now = 0
for i in range(n):
    now += a[i]
    maxp = max(maxp, now)
    minp = min(minp, now)
print(max(0, w - maxp + minp + 1))
