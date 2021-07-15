N, M, K = list(map(int, input().split()))
mod = 998244353

c = 1
answer = 0

for i in range(K+1):
    answer += (M * c  * pow(M-1, N - i - 1, mod)) % mod
    answer %= mod
    c = (c * (N-i-1) * pow(i+1, mod-2, mod)) % mod
    
print(answer)
