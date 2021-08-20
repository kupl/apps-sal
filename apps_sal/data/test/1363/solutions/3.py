import bisect


def count(a, low):
    top = low * 2
    lowi = bisect.bisect_left(a, low)
    topi = bisect.bisect_right(a, top)
    return topi - lowi


(gn, dn, fn) = map(int, input().split())
g = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
g = sorted(g)
d = sorted(d)
f = sorted(f)
ans = 0
for x in g:
    dc = count(d, x)
    fc = count(f, x)
    ans += dc * (dc - 1) * fc * (fc - 1) * (fc - 2) // 12
for x in d:
    gc = count(g, x)
    dc = count(d, x)
    fc = count(f, x)
    ans += gc * (dc - 1) * fc * (fc - 1) * (fc - 2) // 6
for x in f:
    gc = count(g, x)
    dc = count(d, x)
    fc = count(f, x)
    ans += gc * dc * (dc - 1) * (fc - 1) * (fc - 2) // 4
print(ans)
