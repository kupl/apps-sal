B = 10**9 + 7
a = 3


def binpow(n):
    if n == 1:
        return a
    if (n & 1) == 0:
        u = binpow(n >> 1)
        return (u * u) % B
    else:
        return (binpow(n - 1) * a) % B


n = int(input())
u = binpow(n + n + n)
a = 7
v = binpow(n)
print((u + B - v) % B)
