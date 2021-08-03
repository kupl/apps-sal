n = int(input())


def ans(x, y, a, b, k):
    if ch(x, y, a, b, len(v)) < k:
        return -1
    l, r = -1, len(v)
    while l + 1 != r:
        m = (l + r) // 2
        if ch(x, y, a, b, m) >= k:
            r = m
        else:
            l = m
    return r


def nok(a, b):
    s, d = a, b
    while b:
        a, b = b, a % b
    return (s * d) // a


def ch(x, y, a, b, m):
    ab = m // nok(a, b)
    a = m // a - ab
    b = m // b - ab
    if x > y:
        s = sum(v[0:ab]) * (x + y) + sum(v[ab:ab + a]) * x + sum(v[ab + a:ab + a + b]) * y
    else:
        s = sum(v[0:ab]) * (x + y) + sum(v[ab:ab + b]) * y + sum(v[ab + b:ab + a + b]) * x
    return s


for _ in range(n):
    input()
    v = sorted(list([int(x) // 100 for x in input().split()]), key=lambda x: -x)
    x, a = [int(x) for x in input().split()]
    y, b = [int(x) for x in input().split()]
    k = int(input())
    print(ans(x, y, a, b, k))
