n, m = map(int, input().split())
p = 10**9 + 7


def pfact(m):
    pf = {}
    for i in range(2, int(m**0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1:
        pf[m] = 1
    return pf


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


N = 3 * 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

# テンプレ終わり

if m == 1:
    print(1)
    return

factlist = pfact(m).values()

ans = 1

for i in factlist:
    ans = ans * cmb(i + n - 1, i, p) % p

print(ans % p)
