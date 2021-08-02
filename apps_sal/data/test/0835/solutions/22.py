def f(x):
    cb = max(0, (tb * x - nb) * pb)
    cs = max(0, (ts * x - ns) * ps)
    cc = max(0, (tc * x - nc) * pc)
    return cc + cs + cb <= rs


s = list(input())
tb, ts, tc = s.count('B'), s.count('S'), s.count('C')
nb, ns, nc = list(map(int, input().split()))
pb, ps, pc = list(map(int, input().split()))
rs = int(input())
l, r = 0, 10**14
while l < r:
    m = (l + r) // 2
    if f(m):
        l = m + 1
    else:
        r = m
print(l - 1)
