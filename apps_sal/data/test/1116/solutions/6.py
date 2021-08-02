from math import ceil


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


t = int(input())
for kkk in range(t):
    a, b, k = map(int, input().split())
    if a == b:
        print('OBEY')
    else:
        g = gcd(a, b)
        a //= g
        b //= g
        a, b = max(a, b), min(a, b)
        kk = (a - 1) // b + (1 if (a - 1) % b != 0 else 0)
        if kk >= k:
            print('REBEL')
        else:
            print('OBEY')
