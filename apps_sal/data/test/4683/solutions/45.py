n = int(input())
a = list(map(int, input().split()))
ans = 0
mod = 10**9 + 7
b = sum(a)

for i in range(n-1):
    b = b-a[i]
    ans += a[i]*b

print(ans%mod)
