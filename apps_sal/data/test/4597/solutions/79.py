N = int(input())
ans = 1
mod = 1000000007
for i in range(1, N + 1):
    ans *= i
    ans %= mod
print(ans)
