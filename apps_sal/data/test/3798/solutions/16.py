import math

n = int(input())
s = int(input())

if n == 1:
    if s == 1:
        print((2))
    else:
        print((-1))
    return

if n == s:
    print((n + 1))
    return

if n < s:
    print((-1))
    return


def ds(N, b):
    ret = 0
    while True:
        N, mod = divmod(N, b)
        ret += mod
        if N == 0:
            return ret


i = 0
for i in range(2, math.floor(n**(1/2)) + 1):
    if ds(n, i) == s:
        print(i)
        return

if i == 0:
    i = math.floor(n**(1/2))
c = n // (i + 1)
for i in range(c, 0, -1):
    if (n-s) % i == 0:
        b = (n-s)//i + 1
        if i < b and 0 <= s-i < b:
            print(b)
            return

print((-1))

