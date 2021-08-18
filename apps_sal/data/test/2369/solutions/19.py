n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))
ans_sum = 0


def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


mod = 10**9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, n + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


for i in range(n):
    a = A[i]
    mi = i
    ma = n - 1 - i
    ans_sum += cmb(mi, k - 1, mod) * a
    ans_sum -= cmb(ma, k - 1, mod) * a
    ans_sum %= mod
print(ans_sum)
