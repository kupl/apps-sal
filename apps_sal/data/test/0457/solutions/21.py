from math import floor, sqrt


def pp(a, b, c):
    r = 1
    a %= c
    while b:
        if b & 1:
            r = r * a % c
        b >>= 1
        a = a * a % c
    return r


(n, x) = [int(i) for i in input().split()]
d = n
l = []
h = floor(sqrt(d))
MOD = 1000000007
if d % 2 == 0:
    l += [2]
    while d % 2 == 0:
        d //= 2
for i in range(3, h + 1, 2):
    if d % i == 0:
        l += [i]
    while d % i == 0:
        d //= i
if d > 2:
    l += [d]
ans = 1
for i in l:
    f = i
    s = 0
    while f <= x:
        s += x // f
        f *= i
    ans = ans * pp(i, s, MOD) % MOD
print(ans)
