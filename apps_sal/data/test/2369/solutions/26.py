from functools import reduce

MOD = 10 ** 9 + 7

n, k = list(map(int, input().split()))
la = list(map(int, input().split()))
la.sort()

f = 1
lf = [1]
for i in range(1, n + 1):
    f = (f * i) % MOD
    lf.append(f)

ii = 1
lii = [0, 1]
fi = 1
lfi = [1, 1]
for i in range(2, n + 1):
    ii = (-lii[MOD % i] * (MOD // i)) % MOD
    fi = (fi * ii) % MOD
    lii.append(ii)
    lfi.append(fi)


def combi(n, k):
    if k < 0:
        return 0
    elif k > n:
        return 0
    else:
        return (lf[n] * lfi[k] * lfi[n - k]) % MOD


def addmod(a, b):
    return (a + b) % MOD


def sumfmax():
    return reduce(addmod, (a * combi(i, k - 1) for i, a in enumerate(la)))


def sumfmin():
    return reduce(addmod, (a * combi(n - i - 1, k - 1) for i, a in enumerate(la)))


answer = (sumfmax() - sumfmin()) % MOD
print(answer)

