def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


q = int(input())
while q > 0:
    n = int(input())
    p = sorted(list(map(int, input().split())), reverse=True)
    (x, a) = map(int, input().split())
    (y, b) = map(int, input().split())
    nsum = int(input())
    (maxper, maxint, minper, minint) = (0, 0, 0, 0)
    if x < y:
        (maxper, minper, maxint, minint) = (y, x, b, a)
    else:
        (maxper, minper, maxint, minint) = (x, y, a, b)
    (left, right, middle) = (0, n + 1, 0)
    while right - left > 1:
        middle = (left + right) // 2
        total = 0
        tlcm = lcm(a, b)
        tlcmk = middle // tlcm
        (tak, tbk) = (middle // maxint - tlcmk, middle // minint - tlcmk)
        cur = 0
        while cur < tlcmk:
            total += p[cur] // 100 * (x + y)
            cur += 1
        while cur < tlcmk + tak:
            total += p[cur] // 100 * maxper
            cur += 1
        while cur < tlcmk + tak + tbk:
            total += p[cur] // 100 * minper
            cur += 1
        if total >= nsum:
            right = middle
        else:
            left = middle
    if right == n + 1:
        print(-1)
    else:
        print(right)
    q -= 1
