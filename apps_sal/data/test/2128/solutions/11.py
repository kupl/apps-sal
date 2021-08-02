import sys
input = sys.stdin.readline
n = int(input())
L = map(int, input().split())
k = 0
c = 1
m = 998244353
counter = 0
for i in L:
    k += c * (pow(100, n - counter, m))
    k %= m
    c *= i
    c %= m
    counter += 1


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x


p = k % m
q = c % m
print((modInverse(q, m) * p) % m)
