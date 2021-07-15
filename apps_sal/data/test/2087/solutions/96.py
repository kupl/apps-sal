num = list(map(int, input().split()))
mod = 998244353
ans = 1
for i in num:
    ans *= i*(i+1)//2
print((ans % mod))

