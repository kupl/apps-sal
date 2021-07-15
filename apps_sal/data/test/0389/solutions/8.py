def gcd(a, b): return gcd(b, a % b) if b else a
a, b = map(int, input().split())
k = 2 ** 30 * 3 ** 19 * 5 ** 13
u, v = gcd(k, a), gcd(k, b)
if a * v != b * u: print(-1)
else:
    s, c = 0, u * v // (gcd(u, v) ** 2)
    for i in [2, 3, 5]:
        while c % i == 0:
            c //= i
            s += 1
    print(s)
