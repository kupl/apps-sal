n,k = map(int,input().split())
mod = 10**9+7
a = 1
b = n-k+1
for i in range(k):
    ans = a*b % mod
    print(ans)
    a = a * (k-1-i)//(i+1)
    b = b * (n-k-i)//(i+2)
