from math import gcd
n = int(input())
if n == 1:
    print(1)
    return
elif n == 2:
    print(2)
    return
else:
    d = 0
    for i in range(2, n):
        if i * i > n:
            break
        if (n % i) == 0:

            d = gcd(d, i)
            d = gcd(d, n // i)
if d:
    print(d)
else:
    print(n)
