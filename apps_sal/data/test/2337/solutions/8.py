from bisect import bisect_left


def binr(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    if pos < hi:
        return pos
    else:
        return -1


n, m = map(int, input().split())
d = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
fl = True
ans = 0
for i in d:
    if (i not in a):
        fl = False
if fl == True:
    print(0)
    return
for i in range(n):
    if d[i] in a:
        d[i] = 0
    r = binr(a, d[i])
    if r == -1:
        ans += 1
    else:
        a[r] = -1
    a.sort()
print(ans)
