(a, b, x, y) = list(map(int, input().split()))
if a == b:
    print(x)
else:
    res = 100000000000000000
    if a != 1:
        aa = a - 1
        tmp = x
        tmp += y * (aa - b)
        res = min(res, tmp)
    tmp = x
    tmp += y * abs(a - b)
    res = min(res, tmp)
    if a == b:
        res = min(x, res)
    elif a > b:
        res = min(res, x * (abs(a - b) * 2 - 1))
    elif a < b:
        res = min(res, x * (abs(a - b) * 2 + 1))
    print(res)
