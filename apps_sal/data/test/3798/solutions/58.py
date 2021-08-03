from math import sqrt


def digitsum(b, n):
    if b > n:
        return n
    else:
        return digitsum(b, n // b) + n % b


def divisors(M):  # Mの約数列 O(n^(0.5+e))
    import math
    d = []
    i = 1
    while math.sqrt(M) >= i:
        if M % i == 0:
            d.append(i)
            if i**2 != M:
                d.append(M // i)
        i = i + 1
    d.sort()
    return d


n = int(input())
s = int(input())
if 0 > n - s:
    print((-1))
else:
    m = int(sqrt(n))
    for b in range(2, m + 1):
        if digitsum(b, n) == s:
            print(b)
            break
    else:
        d = divisors(n - s)
        for i in d:
            if i >= m and s >= (n - s) // i and i + 1 > (s - (n - s) // i):
                print((i + 1))
                break
        else:
            if n == s:
                print((n + 1))
            else:
                print((-1))
