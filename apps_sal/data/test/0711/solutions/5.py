def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


def cmb(n, r, mod):
    a = 1
    b = 1
    r = min(r, n - r)
    for i in range(r):
        a = a * (n - i) % mod
        b = b * (i + 1) % mod
    return a * pow(b, mod - 2, mod) % mod


(N, M) = map(int, input().split())
MOD = 10 ** 9 + 7
f = factorization(M)
ans = 1
for (i, j) in f:
    ans *= cmb(j + N - 1, j, MOD)
    ans %= MOD
if M == 1:
    ans = 1
print(ans)
