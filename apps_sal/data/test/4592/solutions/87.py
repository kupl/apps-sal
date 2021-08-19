MOD = 10 ** 9 + 7


def sieve(n):
    srn = int(n ** 0.5) + 1
    f = [False] * (srn + 1)
    res = []
    for i in range(2, srn + 1):
        if f[i]:
            continue
        res.append(i)
        for j in range(2 * i, srn + 1, i):
            f[j] = True
    return res


def trial_division(n):
    res = dict()
    for i in range(2, n + 1):
        m = i
        pn = sieve(m)
        for p in pn:
            while m % p == 0:
                res[p] = res.get(p, 0) + 1
                m //= p
        if m > 1:
            res[m] = res.get(m, 0) + 1
    return res


N = int(input())
fn = trial_division(N)
res = 1
for f in fn.values():
    res *= f + 1
    res %= MOD
print(res)
