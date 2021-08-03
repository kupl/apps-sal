import bisect
n, m = list(map(int, input().split()))
a = []
b = []
for i in range(m):
    s, d, c = list(map(int, input().split()))
    if c > d - s + 1:
        print(-1)
        quit()
    l = bisect.bisect_left(b, d)
    a.insert(l, [s, d, c, i + 1])
    b.insert(l, d)
ds = list('0' for i in range(n))
for i in range(m):
    s, d, c, mi = a[i]
    c0 = 0
    for j in range(s, d):
        if ds[j - 1] == '0':
            ds[j - 1] = str(mi)
            c0 += 1
        if c0 >= c:
            break
    if c0 < c:
        print(-1)
        quit()
    ds[d - 1] = str(m + 1)
print(' '.join(ds))
