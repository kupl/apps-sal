import math
A, B = map(int, input().split())
x = math.gcd(A, B)


def prime_decomposition(x):
    i = 2
    ls = []
    while i * i <= x:
        while x % i == 0:
            x /= i
            ls.append(i)
        i += 1
    if x > 1:
        ls.append(x)
    return ls


cnt = len(set(prime_decomposition(x)))

print(cnt + 1)
