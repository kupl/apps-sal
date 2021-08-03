a, b = list(map(int, input().split(' ')))
lo = 1
hi = 1000000000
while (lo < hi):
    mid = (lo + hi) // 2
    x = mid // 2
    y = mid // 3
    z = mid // 6
    x -= z
    y -= z
    t = 0
    if x <= a:
        t += a - x
    if y <= b:
        t += b - y
    if t > z:
        lo = mid + 1
    else:
        hi = mid
print(lo)
