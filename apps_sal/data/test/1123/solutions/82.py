n,k = map(int,input().split())
mod = 1000000007
cnt = [0]*(k+1)
for i in range(1,k+1)[::-1]:
    cnt[i] = pow(k//i,n,mod)
    for j in range(2*i,k+1,i):
        cnt[i] -= cnt[j]
        cnt[i] %= mod
ans = 0
for i in range(1,k+1):
    ans += cnt[i]*i
    ans %= mod
print(ans)
