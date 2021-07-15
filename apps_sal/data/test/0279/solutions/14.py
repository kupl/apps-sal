def check(k, v, v2, t, d):
    if (t - k - 1) * d >= abs(v2 - v):
        return 1
    else:
        return 0
v1, v2 = map(int, input().split())
t, d = map(int, input().split())
v1, v2 = min(v1, v2), max(v1, v2)
k, v, s = 0, v1, v1
if d == 0:
    print (v1 * t)
else:
    while check(k, v, v2, t, d) == 1:
        k += 1
        v += d
        s += v
    s -= v
    k -= 1
    v = (t - k - 2) * d + v2
    while v > v2:
        s += v
        v -= d
    if v == v2:
        s += v
    if v != v2:
        v += d
        s -= v
        s += v2
    print (s)
