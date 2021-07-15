n, k = list(map(int, input().split()))

mod = 10**9 + 7
cnt = [0]*(k + 1)
ans = 0
for i in range(k, 0, -1):
    cnt[i] = (pow(k//i, n, mod) - sum(cnt[2*i:k+1:i])) % mod
    ans = (ans + i*cnt[i]) % mod

print(ans)

