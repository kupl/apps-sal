def main():
    N, k = map(int, input().split())

    MAX_N = 3 * 10 ** 5
    MOD = 10 ** 9 + 7
    fac = [0]*MAX_N
    inv = [0]*MAX_N
    finv = [0]*MAX_N
    fac[0] = 1; fac[1] = 1
    inv[1] = 1
    finv[0] = 1; finv[1] = 1

    def com_init():
        for i in range(2, MAX_N):
            fac[i] = fac[i-1] * i % MOD
            inv[i] = -(MOD//i)*inv[MOD%i]%MOD
            finv[i] = finv[i-1]*inv[i]%MOD

    def com(n, k):
        if n < 0:return 0
        elif k > n: return 0
        
        return (fac[n]*finv[n-k]%MOD)*finv[k]%MOD
    
    k = min(k, N-1)
    ans = 1
    com_init()
    for i in range(1, k+1):
        ans += com(N, i)*com(N-1, N-i-1)
        ans %= MOD
    print(ans)


def __starting_point():
    main()
__starting_point()
