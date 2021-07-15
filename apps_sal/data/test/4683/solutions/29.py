n = int(input())
a = list(map(int, input().split()))
s = [0]*(n+1)
mod = 10**9 + 7
for i in range(1,n+1):
    s[i] = s[i-1] + a[i-1]
ans = 0
for j in range(1,n):
    ans += a[j-1]*(s[n]-s[j])
print(ans%mod)
