def lsearch(arr, v):
    if arr[0] > v:
        return None
    l = 0
    r = len(arr) - 1
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] > v:
            r = m
        else:
            l = m
    if arr[r] <= v:
        return arr[r]
    return arr[l]


def rsearch(arr, v):
    if arr[-1] < v:
        return None
    l = 0
    r = len(arr) - 1
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] >= v:
            r = m
        else:
            l = m
    if arr[l] >= v:
        return arr[l]
    return arr[r]


def lcost(start, s, b):
    l = lsearch(b, start)
    r = rsearch(b, start)
    if l is None:
        l = r
    if r is None:
        r = l
    vl = abs(start - l) + abs(s[-1] - l) + abs(s[0] - s[-1])
    vr = abs(start - r) + abs(s[-1] - r) + abs(s[0] - s[-1])
    return min(vl, vr)


def rcost(start, s, b):
    l = lsearch(b, start)
    r = rsearch(b, start)
    if l is None:
        l = r
    if r is None:
        r = l
    vl = abs(start - l) + abs(s[0] - l) + abs(s[0] - s[-1])
    vr = abs(start - r) + abs(s[0] - r) + abs(s[0] - s[-1])
    return min(vl, vr)


(n, m, k, q) = map(int, input().split())
ss = [[] for _ in range(n)]
for _ in range(k):
    (r, c) = map(int, input().split())
    ss[r - 1].append(c - 1)
bs = list(map(lambda x: int(x) - 1, input().split()))
bs.sort()
for row in ss:
    row.sort()
lc = 0
rc = 0
l = 0
r = 0
if ss[0]:
    l = ss[0][-1]
    r = ss[0][-1]
    lc = rc = l
top = 0
for (ind, s) in enumerate(ss[1:]):
    if s:
        nlc = min(lcost(l, s, bs) + lc, lcost(r, s, bs) + rc)
        nrc = min(rcost(l, s, bs) + lc, rcost(r, s, bs) + rc)
        lc = nlc
        rc = nrc
        l = s[0]
        r = s[-1]
        top = ind + 1
res = min(lc, rc) + top
print(res)
