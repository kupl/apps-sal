N = int(input())
MOD = 1000000007
ans = 1
for i in range(1, N + 1):
    ans *= i
    ans %= MOD
print(ans)
