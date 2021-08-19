def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
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


(n, m) = map(int, input().split())
chk = factorization(m)


def make_array_for_comb(N, mod=10 ** 9 + 7):
    fact = [1, 1]
    fact_inv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fact.append(fact[-1] * i % mod)
        inv.append(-inv[mod % i] * (mod // i) % mod)
        fact_inv.append(fact_inv[-1] * inv[i] % mod)
    return (fact, fact_inv)


def comb(n, r, mod=10 ** 9 + 7):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n - r] % mod


mod = 10 ** 9 + 7
ans = 1
for i in chk:
    (fact, fact_inv) = make_array_for_comb(i[1] + n - 1, mod)
    ans *= comb(i[1] + n - 1, i[1], mod)
    ans %= mod
if m == 1:
    ans = 1
print(ans)
