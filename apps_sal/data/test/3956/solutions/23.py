MOD = 998244353
(k, n) = list(map(int, input().split()))
facts = [1]
invs = [1]
pow2 = [1]
for i in range(1, n + k):
    f = i * facts[i - 1] % MOD
    facts.append(f)
    invs.append(pow(f, MOD - 2, MOD))
    pow2.append(2 ** i % MOD)


def nCk(n, k):
    return facts[n] * invs[k] * invs[n - k] % MOD


def nHk(n, k):
    return nCk(n + k - 1, n - 1)


ans = []
for i in range(2, k + 2):
    p = i // 2
    ans_i = 0
    for q in range(min(p + 1, n + 1)):
        if k - i + q < 0:
            continue
        if i % 2 > 0:
            ans_i = ans[-1]
            break
        else:
            ans_iq = 0
            if q > 0 and k - i + q > 0:
                ans_iq = (ans_iq + pow2[q - 1] * nCk(p - 1, q - 1) * nHk(k - (i - 1) + (q - 1), n - q)) % MOD
            if q < p:
                ans_iq = (ans_iq + pow2[q] * nCk(p - 1, q) * nHk(k - (i - 1) + q, n - q)) % MOD
        ans_i = (ans_i + ans_iq) % MOD
    ans.append(ans_i)
for a in ans + ans[-2::-1]:
    print(a)
