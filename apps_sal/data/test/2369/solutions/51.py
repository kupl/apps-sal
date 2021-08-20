mod = 10 ** 9 + 7


def prepare(n, mod):
    facts = [1] * (n + 1)
    for i in range(1, n + 1):
        facts[i] = facts[i - 1] * i % mod
    invs = [1] * (n + 1)
    invs[n] = pow(facts[n], mod - 2, mod)
    for i in range(0, n)[::-1]:
        invs[i] = invs[i + 1] * (i + 1) % mod
    return (facts, invs)


def make_combi(facts, invs, n, r, mod):
    return facts[n] * invs[r] * invs[n - r] % mod


(n, k) = map(int, input().split())
a = list(map(int, input().split()))
(facts, invs) = prepare(n, mod)
a.sort()
mi_sum = 0
ma_sum = 0
for (i, j) in enumerate(a):
    if i + 1 >= k:
        ma_sum += j * make_combi(facts, invs, i, k - 1, mod)
        ma_sum %= mod
    if n - i >= k:
        mi_sum += j * make_combi(facts, invs, n - i - 1, k - 1, mod)
        mi_sum %= mod
print((ma_sum - mi_sum) % mod)
