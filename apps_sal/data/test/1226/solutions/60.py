(n, a, b) = map(int, input().split())
p = 10 ** 9 + 7


def cmb(n, r):
    nume = 1
    for i in range(n - r + 1, n + 1):
        nume = nume * i % p
    deno = 1
    for j in range(1, r + 1):
        deno = deno * j % p
        d = pow(deno, p - 2, p)
    return nume * d


nca = cmb(n, a)
ncb = cmb(n, b)
res = pow(2, n, p) - nca - ncb - 1
print(res % p)
