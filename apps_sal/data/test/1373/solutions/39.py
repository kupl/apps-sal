N, K = map(int, input().split())

MOD = 10**9 + 7
n_sum = [0]

for i in range(N):
    n_sum.append(n_sum[i] + i+1)
#print(n_sum)

ans = 0
for i in range(K-1,N):
    #print(n_sum[i], n_sum[N]-n_sum[N-i-1])
    ans += (n_sum[N] - n_sum[N-i-1] - n_sum[i] + 1)
    ans %= MOD

print((ans+1)%MOD)
