(a, b, x) = map(int, input().split())
lo = 1
hi = 10 ** 9
idx = 0
while lo <= hi:
    idx = (lo + hi) // 2
    m = a * idx + b * len(str(idx))
    if m == x:
        hi = idx
        break
    elif m > x:
        hi = idx - 1
    else:
        lo = idx + 1
print(hi)
