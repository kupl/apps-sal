mod = 119 << 23 | 1
n, m, l, r = list(map(int, input().split()))
a = (r + 1) // 2 - l // 2
b = r - l + 1 - a
if a > b: a, b = b, a
t = n * m
if t % 2:
    print(pow(a + b, t, mod))
elif a == b:
    print(pow(a, t, mod) * pow(2, t - 1, mod) % mod)
else:
    print(pow(2, mod - 2, mod) * (1 + pow(2 * a + 1, t, mod)) % mod)
