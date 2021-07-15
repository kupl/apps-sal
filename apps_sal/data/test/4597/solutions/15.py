n = int(input())
mod = 10**9+7
ans = 1
for i in range(n):
    ans *= i+1
    ans = ans%mod
print(ans)
