from math import sqrt


def p_divs(n):
    _a = []
    for _i in range(2, int(sqrt(n)) + 10):
        while n % _i == 0:
            _a.append(_i)
            n //= _i
    if n > 1:
        _a.append(n)
    return _a


(l, r, x, y) = list(map(int, input().split()))
if y % x != 0:
    print(0)
else:
    m = y // x
    divs = p_divs(m)
    d = dict()
    for p in divs:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    p = []
    for k in d:
        p.append((k, d[k]))
    ans = 0
    for i in range(2 ** len(p)):
        (a, b) = (x, x)
        for k in range(len(p)):
            if i // 2 ** k % 2 == 1:
                a *= p[k][0] ** p[k][1]
            else:
                b *= p[k][0] ** p[k][1]
        if a >= l and a <= r and (b >= l) and (b <= r):
            ans += 1
    print(ans)
