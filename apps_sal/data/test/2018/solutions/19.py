def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n, m, q = list(map(int, input().split()))
g = gcd(n, m)
al = n * m // g
xx = al // m
yy = al // n


while (q > 0):
    q -= 1
    x1, y1, x2, y2 = list(map(int, input().split()))
    if (x1 == 1):
        a1 = (y1 - 1) // xx + 1
    else:
        a1 = (y1 - 1) // yy + 1

    if (x2 == 1):
        a2 = (y2 - 1) // xx + 1
    else:
        a2 = (y2 - 1) // yy + 1

    if (a1 == a2):
        print('YES')
    else:
        print('NO')
