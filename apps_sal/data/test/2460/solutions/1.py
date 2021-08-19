(n, m) = list(map(int, input().split()))
xs = list(map(int, input().split()))
ts = list(map(int, input().split()))
ps = [x for (x, t) in zip(xs, ts) if t == 0]
ds = [x for (x, t) in zip(xs, ts) if t == 1]
ans = [0] * m
di = 0
for (pi, p) in enumerate(ps):
    while di < m - 1 and abs(ds[di] - p) > abs(ds[di + 1] - p):
        di += 1
    if di >= m:
        ans[m - 1] += n - pi
        break
    ans[di] += 1
print(' '.join(map(str, ans)))
