def gcd(a, b):
    """最大公約数"""
    (a, b) = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def prime_factorization(x):
    """素因数分解"""
    import math
    re = []
    i = 2
    while x != 1:
        if x % i == 0:
            re.append(i)
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.append(x)
                break
    return re


def solve(A, B):
    div = gcd(A, B)
    print(len(set(prime_factorization(div))) + 1)


def __starting_point():
    (A, B) = list(map(int, input().split()))
    solve(A, B)


__starting_point()
