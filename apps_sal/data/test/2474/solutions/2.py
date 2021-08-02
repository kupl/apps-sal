n = int(input())
C = list(map(int, input().split()))
C = sorted(C, reverse=True)
mod = 10**9 + 7
a = pow(2, 2 * n - 2, mod)
ans = 0
for i in range(n):
    ans = ans + C[i] * (i + 2) * a
print(ans % mod)
