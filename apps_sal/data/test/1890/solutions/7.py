mod = 1000000007


def inv_mod(a, m):
    a %= m
    return pow(a, m - 2, m)


a = input()
k = int(input())
t = len(a)
d = 0
i = 1
for c in a:
    if c in ('0', '5'):
        d = (d + i) % mod
    i = i * 2 % mod
print(d * (pow(2, k * t % (mod - 1), mod) - 1) * inv_mod(pow(2, t, mod) - 1, mod) % mod)
