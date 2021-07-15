K, N = map(int, input().split())
MOD = 998244353

P = N+K
fact = [1]*(P+1)
rfact = [1]*(P+1)
for i in range(P):
    fact[i+1] = r = ((i+1) * fact[i]) % MOD
    rfact[i+1] = pow(r, MOD-2, MOD)

def comb(n, k):
    return fact[n] * rfact[k] * rfact[n-k] % MOD

V = [1]*(P+1)
r = 1
for i in range(P):
    r = (r * 2) % MOD
    V[i+1] = r * rfact[i+1] % MOD

memo = {}
def calc(A):
    if A in memo:
        return memo[A]
    M = A//2
    r = 0
    if A % 2:
        p = K - 2*M + N - 2
        for m in range(max(0, 2*M+2-K), min(M, N-1)+1):
            r += V[m] * rfact[M-m] * (fact[p]*rfact[N-m] + fact[p-1]*rfact[N-m-1])*rfact[p-N+m] % MOD

        if 2*M+2-K <= N <= M:
            r += V[N] * rfact[M-N] % MOD
        r *= fact[M]
    else:
        p = K - 2*M + N - 1
        for m in range(max(0, 2*M+1-K), min(N, M)+1):
            r += V[m] * rfact[M-m] * rfact[N-m] * rfact[p-N+m] % MOD
        r *= fact[M] * fact[p]
    r = memo[A] = r % MOD
    return r
ans = []
for i in range(2, 2*K+1):
    if i <= K:
        ans.append(calc(i - 1))
    else:
        ans.append(calc(2*K - i + 1))
print(*ans, sep='\n')

