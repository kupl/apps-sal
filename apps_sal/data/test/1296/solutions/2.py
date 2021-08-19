n, s = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))


def tr(m):
    bb = [x + (i + 1) * m for (i, x) in enumerate(b)]
    bb = sorted(bb)
    res = sum(bb[:m])

    if res <= s:
        return res
    else:
        return None


res = None
lo = 0
hi = n

d = {}
maxgood = -1

while lo < hi:
    mid = (lo + hi) // 2
    #print("\nl m h", lo, mid, hi)
    temp = tr(mid)
    d[mid] = temp
    if temp is not None:
        lo = mid + 1
        maxgood = max(maxgood, mid)
    else:
        hi = mid
    #print("new l m h", lo, mid, hi, "\n")

temp = tr(hi)
d[hi] = temp
if temp is not None:
    maxgood = max(maxgood, hi)

temp = tr(lo)
d[lo] = temp
if temp is not None:
    maxgood = max(maxgood, lo)

temp = tr(mid)
d[mid] = temp
if temp is not None:
    maxgood = max(maxgood, mid)

print(maxgood, d[maxgood])
