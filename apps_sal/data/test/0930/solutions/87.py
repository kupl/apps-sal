import sys
n, k = list(map(int, input().split()))

sys.setrecursionlimit(2147483647)


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10**9 + 7  # 割る数
N = 2 * n + 1  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = 1

if k > n:
    ans = cmb(n + n - 1, n, p)

else:

    for i in range(1, k + 1):
        ans += (cmb(n, i, p) * cmb(n - 1, n - i - 1, p)) % p

        #print(i,cmb(n, i, p),cmb(n-1,n-i-1,p))

print((ans % p))
