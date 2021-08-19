from math import sqrt


def mcd(x, y):
    if y == 0:
        return x
    else:
        return mcd(y, x % y)


def prime_divisor(x):
    for p in range(2, int(sqrt(x)) + 1):
        if x % p == 0:
            return p
    return x


n = int(input())
(a1, b1) = list(map(int, input().split()))
(a, b) = (a1, b1)
for i in range(2, n + 1):
    (ai, bi) = list(map(int, input().split()))
    a = mcd(ai * bi, a)
    b = mcd(ai * bi, b)
if a != 1:
    print(prime_divisor(a))
elif b != 1:
    print(prime_divisor(b))
else:
    print(-1)
