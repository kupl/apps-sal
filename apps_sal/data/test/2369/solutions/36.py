MOD = 10**9 + 7

N, K = list(map(int, input().split()))
As = list(map(int, input().split()))

def getInvs(n, MOD):
    invs = [1] * (n+1)
    for x in range(2, n+1):
        invs[x] = (-(MOD//x) * invs[MOD%x]) % MOD
    return invs
invs = getInvs(N, MOD)
def getCombKs(n, k, invs, MOD):
    combKs = [0] * (n+1)
    combKs[k] = 1
    for x in range(k+1, n+1):
        combKs[x] = (combKs[x-1] * x * invs[x-k]) % MOD
    return combKs
combKs = getCombKs(N, K-1, invs, MOD)

As.sort()

ans = 0
for i, A in enumerate(As):
    if i >= K-1:
        ans += combKs[i] * A
    if N-1-i >= K-1:
        ans -= combKs[N-1-i] * A
    ans %= MOD

print(ans)

