def modpow(a, n, p):
    if n == 1:
        ans = a % p
    else:
        if n % 2 == 0:
            ans = (modpow(a, n // 2, p) ** 2) % p
        else: # n % 2 == 1
            ans = (a * (modpow(a, n // 2, p) ** 2)) % p

    return ans

p = 10 ** 9 + 7
n, a, b = [int(x) for x in input().split()]

tot = modpow(2, n, p)

Xa, Ya = 1, 1
for i in range(a):
    Xa = (Xa * (n - i)) % p
    Ya = (Ya * (i + 1)) % p
Za = modpow(Ya, p - 2, p)
nCa = (Xa * Za) % p

Xb, Yb = 1, 1
for i in range(b):
    Xb = (Xb * (n - i)) % p
    Yb = (Yb * (i + 1)) % p
Zb = modpow(Yb, p - 2, p)
nCb = (Xb * Zb) % p

ans = (tot - nCa -nCb - 1) % p

print(ans)
