(N, K) = map(int, input().split())
huga = list(map(int, input().split()))
new_list_reverse = sorted(huga, reverse=True)


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
Ni = 10 ** 5 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, Ni + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)
s = 0
for i in range(0, N - K + 1):
    s += new_list_reverse[i] * cmb(N - i - 1, K - 1, 10 ** 9 + 7)
for i in range(K - 1, N):
    s -= new_list_reverse[i] * cmb(i, K - 1, 10 ** 9 + 7)
print(s % (10 ** 9 + 7))
