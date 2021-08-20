def cmb(a, b, c):
    b = min(b, a - b)
    num = 1
    for i in range(b):
        num = num * (n - i) % c
    den = 1
    for i in range(b):
        den = den * (i + 1) % c
    return num * pow(den, -1, c) % c


mod = 10 ** 9 + 7
(n, a, b) = map(int, input().split())
ans = (pow(2, n, mod) - cmb(n, a, mod) - cmb(n, b, mod) - 1) % mod
if ans < 0:
    ans = ans + mod
print(ans)
