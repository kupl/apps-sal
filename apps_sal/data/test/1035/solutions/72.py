import math


def factorize(n):
    V = [1]
    if n == 1:
        return V

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            V.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        V.append(n)
    return V


A, B = [int(x) for x in input().split()]
V = factorize(math.gcd(A, B))
print((len(V)))

