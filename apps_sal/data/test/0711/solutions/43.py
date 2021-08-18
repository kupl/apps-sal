n, m = list(map(int, input().split()))
mod = 10**9 + 7
modp = mod
max_n = 10 ** 6 + 1
fact = [1, 1] + [0] * max_n
factinv = [1, 1] + [0] * max_n
inv = [0, 1] + [0] * max_n


def cmb(n, r, p):
    assert n < p, 'n is less than modp'
    assert n < max_n, 'n in less than max_n'
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return (fact[n] * (factinv[r] * factinv[n - r]) % p) % p


for i in range(2, max_n + 1):
    fact[i] = (fact[i - 1] * i) % modp
    inv[i] = (-inv[modp % i] * (modp // i)) % modp
    factinv[i] = (factinv[i - 1] * inv[i]) % modp


def factorization(m):
    arr = []
    temp = m
    for i in range(2, int(-(-m**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])
    return arr


arr = factorization(m)

ans = 1
for k, v in arr:
    temp = cmb(v + n - 1, n - 1, mod)
    ans = (ans * temp) % mod
if m == 1:
    print((1))
else:
    print(ans)
