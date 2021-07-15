def factorization(n):
    arr = dict()
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt

    if temp != 1:
        arr[temp] = 1

    if not arr and n != 1:
        arr[n] = 1

    return arr


MOD = 10 ** 9 + 7
MAX = 10 ** 5 + 50
modinv = lambda a, mod=10 ** 9 + 7: pow(a, mod - 2, mod)
fac, inv = [1] * MAX, [1] * MAX
for i in range(1, MAX):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = modinv(fac[i])
comb = lambda n, k: fac[n] * inv[k] * inv[n - k] % MOD

N, M = list(map(int, input().split()))
ans = 1
for v in list(factorization(M).values()):
    ans = (ans * comb(N + v - 1, v) % MOD)
print(ans)

