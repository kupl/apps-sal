N = int(input())
C = list(map(int, input().split()))
mod = 10**9 + 7
C.sort()
C.reverse()
ans = 0
for i in range(N):
    ans += C[i] * (i + 2)
    ans %= mod

p = pow(4, N - 1, mod)
ans = ans * p % mod
print(ans)
