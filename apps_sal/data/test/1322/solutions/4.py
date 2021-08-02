MOD = 10**9 + 7

fact = [1] * 2000004
for i in range(1, 2000004):
    fact[i] = (fact[i - 1] * i) % MOD


def C(n, k):
    return (fact[n] * pow(fact[k], MOD - 2, MOD)**2) % MOD


x = int(input()) + 1
res = C(x * 2, x) - 1
print(res)
