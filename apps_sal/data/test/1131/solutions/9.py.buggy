a, b, w, x, c = list(map(int, input().split()))
if c <= a:
    print(0)
    return
l, r = 0, (c - a) * int(1e4)
while l + 1 < r:
    m = (l + r) // 2
    if c - m <= a - (w - b - 1 + m * x) // w:
        r = m
    else:
        l = m
print(r)
