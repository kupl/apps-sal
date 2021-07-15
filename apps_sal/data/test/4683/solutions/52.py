N = int(input())
A = [int(a) for a in input().split()]
mod = 10**9+7

L = [0]*(N+1)
for i in range(N):
    L[i+1] = (L[i]+A[i])%mod

ans = 0
for i in range(N):
    ans += A[i]*(L[-1]-L[i+1])
    ans %= mod
print(ans)
