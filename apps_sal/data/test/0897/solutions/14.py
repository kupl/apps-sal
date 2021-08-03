def rd(): return list(map(int, input().split()))


M = 1000000007
def inv(x): return (M - M // x) * inv(M % x) % M if x - 1 else 1


n, m = rd()
a = list(rd())
b = list(rd())
p, q, r = 0, 1, 1
for i in range(n):
    x, y = a[i], b[i]
    if x == 0 and y == 0:
        p = (p * m * m + r * ((m - 1) * m >> 1)) % M
        q = q * m * m % M
        r = r * m % M
    elif x == 0:
        p = (p * m + r * (m - y)) % M
        q = q * m % M
    elif y == 0:
        p = (p * m + r * (x - 1)) % M
        q = q * m % M
    elif x != y:
        if x > y:
            p = (p + r) % M
        break
print(p * inv(q) % M)
