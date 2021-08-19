def modpow(a, n):
    if n < 1:
        return 1
    ans = modpow(a, n // 2)
    ans = ans * ans % mod
    if n % 2 == 1:
        ans *= a
    return ans % mod


def conb(n, i):
    (inv, ans) = (1, 1)
    for j in range(1, i + 1):
        ans = ans * (n - j + 1) % mod
        inv = inv * j % mod
    return ans * modpow(inv, mod - 2) % mod


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(cnt)
    if temp != 1:
        arr.append(1)
    if arr == []:
        arr.append(1)
    return arr


mod = 10 ** 9 + 7
(N, M) = [int(x) for x in input().rstrip().split()]
fact = factorization(M)
ans = 1
if M == 1:
    print(1)
else:
    for i in fact:
        ans *= conb(i + N - 1, N - 1)
    print(ans % mod)
