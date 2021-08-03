from functools import reduce

N = int(input())
*A, = map(int, input().split())
mod = 10**9 + 7


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


LCM = reduce(lcm, A) % mod

print(sum([LCM * pow(A[i], -1, mod) % mod for i in range(N)]) % mod)
