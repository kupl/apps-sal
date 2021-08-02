N = int(input())
C = list(map(int, input().split()))
for i in range(N):
    C[i] *= -1
C.sort()
for i in range(N):
    C[i] *= -1
mod = 10**9 + 7
ans = 0
for i in range(N):
    ans += C[i] * (i + 2)
ans = ans * (4**(N - 1))
ans = ans % mod
print(ans)
