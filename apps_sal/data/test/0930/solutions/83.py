#部屋にいる人数が０の組み合わせ（nCi）と０でない部屋にいる人数の組み合わせ（(n-1)Ci）の積で求めることが出来る


N, K = list(map(int, input().split()))
K = min(N-1, K)
fact = [1 for _ in range(200001)]
inv = [1 for _ in range(200001)]
fact_inv = [1 for _ in range(200001)]
mod = 10**9+7


for i in range(2, 200001):
    fact[i] = (fact[i-1]*i) % mod
    inv[i] = mod - (inv[mod % i] * (mod // i)) % mod
    fact_inv[i] = (fact_inv[i-1] * inv[i]) % mod


dp = [0] * N

for i in range(N):
    #nCiを求める
    f1 = (fact[N] * fact_inv[N-i] * fact_inv[i]) % mod  

    #(n-1)Ciを求める
    f2 = (fact[N-1] * fact_inv[N-i-1] * fact_inv[i]) % mod 

    #積の計算
    f = (f1*f2)%mod
    
    if i == 0:
        dp[i] = f
    else:
        dp[i] = (dp[i-1] + f) % mod


print((dp[K]))

