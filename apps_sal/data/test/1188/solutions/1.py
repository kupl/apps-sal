from collections import Counter
n = int(input())
a = list(map(int, input().split()))


def get(cnt):
    c = Counter(a)
    last = []
    while c[1] and (cnt is None or len(last) < cnt):
        x = 1
        while c[x]:
            c[x] -= 1
            x *= 2
        last.append(x >> 1)
    rem = sorted(c.elements())
    i = 0
    for x in last[::-1]:
        if i < len(rem) and rem[i] < 2 * x:
            i += 1
    return len(last) if i == len(rem) else 0


mx = get(None)
(lo, hi) = (0, mx)
while lo < hi:
    mid = lo + hi >> 1
    if get(mid):
        hi = mid
    else:
        lo = mid + 1
if mx:
    print(*list(range(lo, mx + 1)))
else:
    print(-1)
