def fast(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return a * fast(a, b - 1) % mod
    x = fast(a, b / 2) % mod
    return x * x % mod


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = 0
q = 1
z1 = 1
z2 = 1
mod = 1000000007
for i in range(0, n):
    if a[i] != 0 and b[i] != 0:
        if a[i] == b[i]:
            continue
        if a[i] > b[i]:
            p = (p * z2 % mod + q * z1 % mod) % mod
            q = q * z2 % mod
        break
    if a[i] == 0 and b[i] != 0:
        p = (p * m * z2 % mod + z1 * q * (m - b[i]) % mod) % mod
        q = q * z2 * m % mod
        z2 = z2 * m % mod
    if a[i] != 0 and b[i] == 0:
        p = (p * m * z2 % mod + z1 * q * (a[i] - 1) % mod) % mod
        q = q * z2 * m % mod
        z2 = z2 * m % mod
    if a[i] == 0 and b[i] == 0:
        p = (p * m * 2 * z2 + z1 * q * (m - 1)) % mod
        q = q * z2 * 2 * m % mod
        z2 = z2 * m % mod
print(p * (fast(q, mod - 2) % mod) % mod)
