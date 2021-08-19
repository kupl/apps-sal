# E_Multiplication4
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 1000000007
# ソート
arr = []
j = 0
i = 0
seki = 1
gyaku = 1
minuscount = 0
minusposition = 0


def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


def modinv(a, mod):
    return modpow(a, mod - 2, mod)


arr = sorted(A, reverse=True)
if arr[(N - 1)] > 0:
    for i in range(K):
        seki = seki * arr[i] % MOD
else:
    if arr[0] < 0:
        for j in range(K):
            if K % 2 == 1:
                seki = seki * arr[j] % MOD
            else:
                seki = seki * arr[N - j - 1] % MOD
    else:
        while (i + j) < K:
            if (i + j + 1) < K:
                if arr[i] * arr[i + 1] > (arr[(N - j - 1)] * arr[(N - j - 2)]):
                    seki = seki * arr[i] % MOD
                    i += 1
                else:
                    minuscount += 2
                    minusposition = N - j - 2
                    seki = (seki * arr[(N - j - 1)] % MOD) * arr[(N - j - 2)] % MOD
                    j += 2
            else:
                if abs(arr[i]) > abs(arr[(N - j - 1)]):
                    seki = seki * arr[i] % MOD
                    i += 1
                else:
                    minuscount += 1
                    minusposition = N - j - 1
                    seki = seki * arr[(N - j - 1)] % MOD
                    j += 1
if (minuscount % 2) != 0:
    if minusposition != (i - 1):
        gyaku = modinv(arr[minusposition], MOD)
        seki = seki * gyaku % MOD
        seki = seki * arr[i] % MOD
print(seki)
