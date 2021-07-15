
N,K = list(map(int, input().split()))
A_list = sorted(list(map(int, input().split())))

if K == 1:
    print((0))
    return

MOD = 10**9 + 7

fact = [0] * (N+1)
fact_inv = [0] * (N+1)
inv = [0] * (N+1)

fact[0] = fact[1]  = 1
fact_inv[0] = fact_inv[1] = 1
inv[1] = 1

for i in range(2, N):
    fact[i] = fact[i-1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD//i) % MOD # //で良いのかな?
    fact_inv[i] = fact_inv[i-1] * inv[i] % MOD

def combo(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fact[n] * (fact_inv[k] * fact_inv[n-k] % MOD) % MOD

def main():
    min_sum = 0
    max_sum = 0

    for i in range(N-K+1):
        cmb = combo(N-i-1, K-1)
        min_sum -= A_list[i] * cmb
        max_sum += A_list[N-i-1] * cmb
        min_sum %= MOD
        max_sum %= MOD
    print(((max_sum+min_sum + MOD )%MOD))
    


def __starting_point():
    main()


__starting_point()
