def I(): return list(map(int, input().split()))


n = I()[0]
d1 = [0] + sorted(I())
m = I()[0]
d2 = [0] + sorted(I())

index1, index2 = {}, {}
index1[0], index2[0] = n, m
i, j = n, m
while (i >= 0 and j >= 0):
    maxd = max(d1[i], d2[j])
    if not(maxd in index1):
        index1[maxd] = n - i
    if not(maxd in index2):
        index2[maxd] = m - j
    if d1[i] == maxd:
        i -= 1
    if d2[j] == maxd:
        j -= 1
while (i >= 0):
    if not(d1[i] in index1):
        index1[d1[i]] = n - i
    i -= 1
while (j >= 0):
    if not(d2[j] in index2):
        index2[d2[j]] = m - j
    j -= 1

a, b, maxdiff = 0, 0, -1e100
for foo in [0] + d1 + d2:
    i = index1[foo]
    j = index2[foo]
    _a, _b = i * 3 + (n - i) * 2, j * 3 + (m - j) * 2
    diff = _a - _b
    if (diff > maxdiff) or (diff == maxdiff and _a > a):
        maxdiff = diff
        a, b = _a, _b
print('%d:%d' % (a, b))
