# Acknowledge: https://atcoder.jp/contests/arc102/submissions/3127544
MOD = 998244353
k, n = list(map(int, input().split()))

facts = [1]
invs = [1]
for i in range(1, n + k):
    f = (i * facts[i - 1]) % MOD
    facts.append(f)
    invs.append(pow(f, MOD - 2, MOD))


def nCk(n, k):
    return (facts[n] * invs[k] * invs[n - k]) % MOD


memo = []
for p in range(1, (k + 3) // 2):
    i = 2 * p + 1
    tmp = 0
    for t in range(min(p + 1, n + 1)):
        if k - i + t < 0:
            continue
        res = nCk(p, t)
        res *= nCk(n + k - i, k - i + t)
        res *= pow(2, t, MOD)
        tmp = (tmp + res) % MOD
    memo.append(tmp)

ans = []
for i in range(1, k):
    ans.append(memo[(i - 1) // 2])
for a in ans + [memo[-1]] + ans[::-1]:
    print(a)
