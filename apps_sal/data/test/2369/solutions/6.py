n, k = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10**9+7
a.sort()

def prepare(n, MOD):
    """
    nCr mod MOD
    :param n:
    :param MOD:
    :return:
    """
    facts = [1]*(n+1)
    for i in range(1, n+1):
        facts[i] = facts[i-1]*i%MOD
    invs = [1]*(n+1)
    _invs = [1]*(n+1)
    invs[n] = pow(facts[n], MOD-2, MOD)
    for i in range(0, n)[::-1]:
        invs[i] = invs[i+1] * (i+1) % MOD
    return facts, invs
facts, invs = prepare(n, MOD)
max_sum = 0
min_sum = 0
for i, v in enumerate(a):
    under = i
    upper = n-1-i
    if i >= k-1:
        max_sum += v*facts[i]*invs[k-1]*invs[i-k+1]
        max_sum %= MOD
    if n-1-i >= k-1:
        min_sum += v*facts[n-1-i]*invs[k-1]*invs[n-i-k]
        min_sum %= MOD

print((max_sum-min_sum)%MOD)
