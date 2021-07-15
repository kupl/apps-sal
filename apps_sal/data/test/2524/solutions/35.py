n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7
ans = 0

for i in range(60):
    cou  = 0
    bit = 1 << i
    for j in a:
        if j & bit:
            cou += 1
    num1 = cou
    num0 = n - num1
    ans += ((num1*num0) * bit )%mod
print(ans%mod)
