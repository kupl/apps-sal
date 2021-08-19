(n, k) = map(int, input().split())
mod = 1000000007
b = mod - 2
blis = []
c = 0
while b > 0:
    if b & 1 == 1:
        blis.append(c)
    c += 1
    b >>= 1


def modinv(a):
    if a == 1:
        return 1
    else:
        res = 1
        li = []
        for _ in range(c):
            li.append(a % mod)
            a = a * a % mod
        for item in blis:
            res = res * li[item] % mod
        return res


if k >= n:
    L = 2 * n - 1
    ansbunsi = 1
    for j in range(n - 1):
        ansbunsi = ansbunsi * L % mod
        L -= 1
    ansbunbo = 1
    L = n - 1
    for j in range(n - 1):
        ansbunbo = ansbunbo * L % mod
        L -= 1
    ansbunbo = modinv(ansbunbo)
    print(ansbunsi * ansbunbo % mod)
else:
    kaijou = [1, 1]
    for j in range(2, n + 1):
        kaijou.append(kaijou[-1] * j % mod)
    ans = 0
    for m in range(k + 1):
        ansbunsi = kaijou[n] * kaijou[n - 1] % mod
        ansbunbo = kaijou[m] * kaijou[n - m] % mod
        ansbunbo = ansbunbo * kaijou[n - m - 1] % mod
        ansbunbo = ansbunbo * kaijou[m] % mod
        ansbunbo = modinv(ansbunbo)
        ans += ansbunbo * ansbunsi
        ans %= mod
    print(ans)
