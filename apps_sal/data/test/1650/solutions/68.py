def powmod(x, n, mod):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % mod
            x = x ** 2 % mod
            n = (n - 1) // 2
        else:
            x = x ** 2 % mod
            n = n // 2 % mod

    return K * x


L = input()
S = len(L) - 1
if S == 0:
    print((3))
else:
    ans = 1
    ct = 0
    for i in range(S + 1):
        if int(L[i]) == 1:
            ans += ((powmod(3, S - i, 10**9 + 7) + 1) * powmod(2, ct, 10**9 + 7)) % (10**9 + 7)
            ans %= (10**9 + 7)
            ct += 1
    print(ans)
