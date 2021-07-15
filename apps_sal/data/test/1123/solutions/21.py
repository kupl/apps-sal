mod = 10 ** 9 + 7
N, K = map(int, input().split())
cnt = [0 for i in range(K+1)]
for i in range(K, 0, -1):
    tmp_sum = pow(K//i, N, mod)
    for j in range(2, 10**7+1):
        if i*j > K:
            break
        tmp_sum -= cnt[i*j]
    cnt[i] = tmp_sum
ans = sum(cnt[i]*i for i in range(1,K+1)) % mod
print(ans)
