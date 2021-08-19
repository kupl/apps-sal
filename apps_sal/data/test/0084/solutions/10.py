from math import factorial as fac


def solve(n):
    if n <= 4:
        return fac(n) // (2 * fac(n - 2))
    m = n + (n - 1)
    x = '9'
    while int(x + '9') <= m:
        x += '9'
    l = []
    for i in range(10):
        if int(str(i) + x) <= m:
            l.append(int(str(i) + x))
    res = 0
    for p in l:
        y = min(p - 1, n)
        res += (y - (p - y) + 1) // 2
    return res


n = int(input())
print(solve(n))
