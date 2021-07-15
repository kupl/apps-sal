
def main():
    n, k = list(map(int, input().split()))

    MOD = 10**9 + 7
    Comb = [None] * (n + 1)
    dp = [[None] * (n + 1) for i in range(n+1)]

    for i in range(1, n + 1):
        Comb[i] = [1] + [(Comb[i-1][j-1] + Comb[i-1][j]) % MOD for j in range(1, i)] + [1]

    def powgen(base):
        cur = 1
        while True:
            yield cur
            cur = cur * base % MOD

    gen, gen_1 = powgen(k), powgen(k - 1)
    kpower = [next(gen) for i in range(n + 1)]
    k1power = [next(gen_1) for i in range(n + 1)]

    dp[1][0] = (kpower[n] - k1power[n] + MOD) % MOD
    for i in range(1, n+1): dp[1][i] = kpower[n-i]

    for r in range(2, n + 1): # row remaining
        # c means col incompleted
        dp[r] = [(dp[r-1][c] * k1power[c] * (kpower[n-c]-k1power[n-c]) + 
            kpower[n-c] * sum([dp[r-1][c-i] * Comb[c][i] * k1power[c-i] for i in range(1, c+1)])) % MOD
            for c in range(n+1)]
    # input 250 1000000000
    return dp[n][n]

print(main())



