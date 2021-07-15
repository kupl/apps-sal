n,k = map(int,input().split())
mod = 10**9 + 7

ans = 1
for i in range(k,n+1):
    low = i*(i-1)//2
    high = n*(n+1)//2 - (n-i)*(n-i+1)//2
    ans += high - low + 1
    ans %= mod
print(ans)
