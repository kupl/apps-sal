import math
a, b = map(int, input().split())
gcd = math.gcd(a, b)


def fctr1(n):
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r + 2):
        while n % i == 0:
            c += 1
            n = n // i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


print(len(fctr1(gcd)) + 1)
