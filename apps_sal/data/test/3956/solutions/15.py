def solve():
    MOD = 998244353
    maxNK = 2000

    K, N = list(map(int, input().split()))

    def getInvs(n, MOD):
        invs = [1] * (n+1)
        for x in range(2, n+1):
            invs[x] = (-(MOD//x) * invs[MOD%x]) % MOD
        return invs

    def getCombss(n, k, invs, MOD):
        def getCombNs(n, k, invs, MOD):
            combNs = [1] * (n//2+1)
            for x in range(1, n//2+1):
                combNs[x] = (combNs[x-1] * (n-x+1) * invs[x]) % MOD
            return (combNs + combNs[:(n+1)//2][::-1])[:k+1]
        combss = [[] for n in range(n+1)]
        for x in range(n+1):
            combss[x] = getCombNs(x, k, invs, MOD)
            combss[x] += [0] * (k+1-len(combss[x]))
        return combss

    invs = getInvs(2*maxNK, MOD)
    combss = getCombss(2*maxNK, maxNK, invs, MOD)

    def getPows(base, n, MOD):
        pows = [1] * (n+1)
        for x in range(1, n+1):
            pows[x] = (pows[x-1] * base) % MOD
        return pows
    pow2s = getPows(2, N, MOD)

    anss = []
    for i in range(2, K+2, 2):
        ans = 0
        numFree = abs(K+1-i)
        numPair = (K-numFree+1)//2
        numPair -= 1
        for x in range(min(numPair, N)+1):
            ans += combss[numPair][x] * pow2s[x] * combss[N+numFree-1][N-x] % MOD
            ans %= MOD
        for x in range(min(numPair, N)+1):
            ans += combss[numPair][x] * pow2s[x] * combss[N+numFree-2][N-x-1] % MOD
            ans %= MOD
        anss.append(ans)
        if i+1 <= K+1:
            anss.append(ans)

    anss = anss + anss[:-1][::-1]
    print(('\n'.join(map(str, anss))))


solve()

