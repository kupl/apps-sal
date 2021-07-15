N, K = map(int, input().split())
mod = 10**9 + 7

def ksum(n):
    return n*(n+1)//2

ans = 0
msum = ksum(N)
for i in range(K, N+2):
    ans += msum - ksum(N - i) - ksum(i-1) + 1
    #print(i, ans)
    ans %= mod

print(ans)
