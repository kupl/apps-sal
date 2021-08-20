""" بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ """
from collections import Counter


def gi():
    return list(map(int, input().split()))


(n,) = gi()
l = gi()
occ = Counter(l)
mid = 0
ans = n
rep = n - len(occ)


def f(x):
    oc = Counter(l)
    for k in range(x):
        oc[l[k]] -= 1
    s = set(oc.values())
    if s == {1} or s == {1, 0}:
        return 1
    for k in range(x, n):
        oc[l[k]] -= 1
        oc[l[k - x]] += 1
        s = set(oc.values())
        if s == {1} or s == {1, 0}:
            return 1
    return 0


(lo, hi) = (0, n)
while lo <= hi:
    mid = (lo + hi) // 2
    if f(mid):
        ans = min(ans, mid)
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)
