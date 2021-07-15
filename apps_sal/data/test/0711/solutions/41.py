MOD = 10**9 + 7
MOD_t_MAX = 3 * (10**5)

fac  = [None] * MOD_t_MAX
finv = [None] * MOD_t_MAX
inv  = [None] * MOD_t_MAX
def MOD_COM_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MOD_t_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
def MOD_COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

def main():
    n, m = map(int, input().split())
    MOD_COM_init()
    dic = {}
    x = 2
    while m%x == 0:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
        m //= x
    x = 3
    while x*x <= m:
        while m%x == 0:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
            m //= x
        x += 2
    if 1 < m:
        if m in dic:
            dic[m] += 1
        else:
            dic[m] = 1
    ans = 1
    for v in dic.values():
        ans *= MOD_COM(n+v-1, v)
        ans %= MOD
    print(ans)

def __starting_point():
    main()
__starting_point()
