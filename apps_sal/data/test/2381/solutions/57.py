MOD = 10**9 + 7


def modpow(a, n):
    r = 1
    while n > 0:
        if n % 2 == 1:
            r = r * a % MOD
        a = a * a % MOD
        n = n // 2
    return r


N, K = map(int, input().split())
As = list(map(int, input().split()))


As.sort(key=lambda x: abs(x), reverse=True)
As_srt = sorted(As)

if N == K or (As_srt[-1] < 0 and K % 2 == 1):
    ans = 1
    for i in range(K):
        ans *= As[N - i - 1]
        ans %= MOD
    print(ans)
else:
    ans = 1
    sign = 1
    for i in range(K):
        ans *= As[i]
        ans %= MOD
        if As[i] < 0:
            sign *= -1
    if sign < 0:
        rm_p = None
        rm_n = None
        for i in range(K):
            if rm_p != None and rm_n != None:
                break
            if rm_p == None and As[K - i - 1] > 0:
                rm_p = As[K - i - 1]
            if rm_n == None and As[K - i - 1] < 0:
                rm_n = As[K - i - 1]

        apd_zp = None
        apd_n = None
        for i in range(N - K):
            if apd_zp != None and apd_n != None:
                break
            if apd_zp == None and As[K + i] >= 0:
                apd_zp = As[K + i]
            if apd_n == None and As[K + i] < 0:
                apd_n = As[K + i]

        if rm_n == None or apd_zp == None:
            rm = rm_p
            apd = apd_n
        elif rm_p == None or apd_n == None:
            rm = rm_n
            apd = apd_zp
        else:
            if abs(rm_p * apd_zp) <= abs(rm_n * apd_n):
                rm = rm_p
                apd = apd_n
            else:
                rm = rm_n
                apd = apd_zp
        ans *= apd
        ans %= MOD
        rm_inv = modpow(rm, MOD - 2)
        ans *= rm_inv
        ans %= MOD

    print(ans)
