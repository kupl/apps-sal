mod = 10**9+7
def comb_lists(n, mod):
    fact = [1 for _ in range(n+1)]
    inv = [1 for _ in range(n+1)]
    fact_inv = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        fact[i] = (fact[i-1]*i) % mod
        inv[i] = mod - (inv[mod % i] * (mod // i)) % mod
        fact_inv[i] = (fact_inv[i-1] * inv[i]) % mod
    
    return fact, fact_inv

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
if K == 1:
    print(0)
    return

for i in range(1, N):
    A[i] += A[i-1]

fact, fact_inv = comb_lists(N, mod)
ans = 0
for i in range(N-K+1):
    s1 = A[N-1] - A[N-2-i]
    s2 = A[i]
    ans += ((fact[N-2-i] * fact_inv[K-2] * fact_inv[N-K-i]) % mod) * (s1 - s2)
    ans = ans % mod
print(ans)
