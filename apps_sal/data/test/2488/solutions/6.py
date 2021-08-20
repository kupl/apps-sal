import bisect
(n, d, a) = map(int, input().split())
mons = []
x_lis = []
for i in range(n):
    (x, h) = map(int, input().split())
    mons.append([x, h])
    x_lis.append(x)
imos = [0 for i in range(n)]
ans = 0
total = 0
x_lis.sort()
mons = sorted(mons, key=lambda x: x[0])
for i in range(n):
    (x, h) = mons[i]
    total -= imos[i]
    h -= total
    if h <= 0:
        continue
    t = (h + a - 1) // a
    ans += t
    total += a * t
    x += 2 * d
    ind = bisect.bisect_right(x_lis, x)
    if ind < n:
        imos[ind] += t * a
print(ans)
