N = int(input())
C = 10**9+7
ans = 1
for i in range(1, N + 1):
    ans *= i
    ans %= C
print(ans)
