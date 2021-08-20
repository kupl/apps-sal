from functools import cmp_to_key
n = int(input())


def dot(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return x1 * x2 + y1 * y2


def cross(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return x1 * y2 - x2 * y1


def top(p):
    (x, y) = p
    return y > 0 or (y == 0 and x > 0)


def polarCmp(p1, p2):
    res = False
    ta = top(p1)
    tb = top(p2)
    if ta != tb:
        res = ta
    else:
        res = cross(p1, p2) > 0
    return -1 if res else 1


def angleLess(a1, b1, a2, b2):
    p1 = (dot(a1, b1), abs(cross(a1, b1)))
    p2 = (dot(a2, b2), abs(cross(a2, b2)))
    return cross(p1, p2) > 0


vals = []
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    vals.append((x, y))
svals = sorted(vals, key=cmp_to_key(polarCmp))
(idx1, idx2) = (0, 1)
for k in range(2, n):
    if angleLess(svals[k - 1], svals[k], svals[idx1], svals[idx2]):
        (idx1, idx2) = (k - 1, k)
if angleLess(svals[n - 1], svals[0], svals[idx1], svals[idx2]):
    (idx1, idx2) = (n - 1, 0)
res1 = res2 = -1
for k in range(n):
    if vals[k] == svals[idx1]:
        res1 = k
    if vals[k] == svals[idx2]:
        res2 = k
print(res1 + 1, res2 + 1)
