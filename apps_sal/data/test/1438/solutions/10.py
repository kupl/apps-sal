n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

lo = 0
hi = 2 * 1e9


def p(cookies):
    powder = k
    for i in range(len(b)):
        have = b[i]
        one = a[i]
        remainder = have - (one * cookies)
        if remainder < 0:
            powder += remainder
    if powder >= 0:
        return True
    return False


while lo < hi:
    m = (lo + hi) // 2
    if p(m):
        lo = m + 1
    else:
        hi = m
print(int(lo if p(lo) else lo - 1))
