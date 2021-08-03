import math
n, a, b = list(map(int, input().split()))
s = 6 * n
if a * b >= s:
    print(a * b)
    print(a, b)
else:
    aa, bb = a, b
    area = float('inf')
    _a = 0
    for i in range(min(math.ceil(s**0.5), s // max(a, b)), min(a, b) - 1, -1):
        _b = math.ceil(s / i)
        _s = _b * i
        if _s <= area:
            area, _a = _s, i
            if _s == s:
                break
    print(area)
    _b = area // _a
    if not (aa <= _a and bb <= _b):
        _a, _b = _b, _a
    print(_a, _b)
