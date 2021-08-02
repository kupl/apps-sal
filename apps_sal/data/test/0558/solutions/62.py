def main():
    # IMPORT MODULE
    #import sys

    # sys.setrecursionlimit(100000)
    #input=lambda :sys.stdin.readline().rstrip()

    # f_inf=float("inf")
    MOD = 998244353

    if 'get_ipython' in globals():
        # SAMPLE INPUT
        n, m, k = 60522, 114575, 7559

    else:
        # INPUT
        #n = input()
        n, m, k = map(int, input().split())

    # SUBMITION CODES HERE
    fac = [1] * (n + 1)
    inv = [1] * (n + 1)

    for i in range(n):
        fac[i + 1] = fac[i] * (i + 1) % MOD  # Calculating the Factorial
        inv[i + 1] = pow(fac[i + 1], MOD - 2, MOD)  # The inverse of the MOD's law (Fermat's Little Theorem)

    def nCr(n, r):
        if 2 * r > n: nCr(n, n - r)
        return fac[n] * inv[r] * inv[n - r] % MOD

    ans = 0
    for i in range(k + 1):
        tmp = nCr(n - 1, i) * m * pow(m - 1, n - 1 - i, MOD)
        ans += tmp
        ans %= MOD
    print(ans)


main()
