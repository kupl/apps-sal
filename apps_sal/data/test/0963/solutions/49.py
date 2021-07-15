import sys
mod = 998244353

N, K = list(map(int, sys.stdin.readline().strip().split()))

step = []
for _ in range(K):
    L, R = list(map(int, sys.stdin.readline().strip().split()))

    step.append((L, R))
step.sort()

dp = [0] * (N + 1)
dp[1] = 1

cusum = [0] * (N + 1)
cusum[1] = 1

for i in range(2, N + 1):
    for L, R in step:
        iter_L = i - R
        iter_R = i - L

        if iter_R <= 0:
            continue
        
        iter_L = max(1, iter_L)

        dp[i] += (cusum[iter_R] - cusum[iter_L - 1]) % mod
    
    cusum[i] = (cusum[i - 1] + dp[i]) % mod

print((dp[N] % mod))

