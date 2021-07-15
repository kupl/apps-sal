__author__ = 'asmn'
a, b, w, x, c = tuple(map(int, input().split()))

if c <= a:
    print(0)
    return
l, r = 0, (c - a) * 10000
while l + 1 < r:
    m = (l + r) // 2

    if c - m <= a - (w - b - 1 + m * x) // w:
        r = m
    else:
        l = m
print(r)
