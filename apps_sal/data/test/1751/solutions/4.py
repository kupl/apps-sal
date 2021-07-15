n = int(input())
MOD = 10 ** 9 + 7
ans1 = 1
ans2 = 1
for i in range(1,n+1):
    ans1 *= i
    ans1 %= MOD
for i in range(n-1):
    ans2 *= 2
    ans2 %= MOD
print((ans1 - ans2) % MOD)
