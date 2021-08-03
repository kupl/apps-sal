from collections import defaultdict as dd
N, k = map(int, input().split())

# 0人の部屋がt個あるとすると、n-t個の部屋にn人がいる。
# k!=1のとき0<=t<=min(k, n-1)
# k==1のときt=1
res = 0
fact = [0] * (N + 1)
ifact = [0] * (N + 1)
inv = [0] * (N + 1)
p = 10**9 + 7

dic = dd(int)


def combination(n, fact, ifact):
    fact[0] = 1
    fact[1] = 1
    ifact[0] = 1
    ifact[1] = 1
    inv[1] = 1
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % p
        inv[i] = p - inv[p % i] * (p // i) % p
        ifact[i] = (ifact[i - 1] * inv[i]) % p


def op(n, k):
    if (n, k) in dic.keys():
        return dic[(n, k)]
    if k < 0 or k > n or n < 0:
        return 0
    dic[(n, k)] = (fact[n] * ifact[k] * ifact[n - k]) % (10**9 + 7)
    return dic[(n, k)]


combination(N, fact, ifact)
for t in range(0, min(k, N - 1) + 1):
    # n-t個の部屋にn人を入れる。ただし、どの部屋にも1人以上いる必要がある
    # n個の部屋のうちどのt個を0人にするかでnCt
    # n-t個の部屋の人数でn-1Cn-t-1
    res += (op(N - 1, N - t - 1) * op(N, t)) % p
print(res % p)
