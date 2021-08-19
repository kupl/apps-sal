def expo(a, n):
    if n > 0:
        ha = expo(a, n // 2)
        if n % 2 == 1:
            return ha * ha * a % MOD
        else:
            return ha * ha % MOD
    else:
        return 1


MOD = 998244353


def f():
    (n, m, L, R) = list(map(int, input().split(' ')))
    height = R - L + 1
    area = n * m
    ans = expo(height, area)
    if area % 2 == 1:
        print(ans)
    elif height % 2 == 0:
        if ans % 2 == 1:
            ans += MOD
        ans //= 2
        print(ans % MOD)
    else:
        if ans % 2 == 0:
            ans += MOD
        ans = (ans + 1) // 2
        print(ans % MOD)


f()
