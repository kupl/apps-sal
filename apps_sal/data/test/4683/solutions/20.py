n = int(input())
A = [int(x) for x in input().split()]
mod = 10 ** 9 + 7
a_cum = [0] * (n + 1)
for i in range(n):
    a_cum[i + 1] = a_cum[i] + A[i]
ans = 0
for i in range(len(A) - 1):
    ans += A[i] * (a_cum[n] - a_cum[i + 1]) % mod
ans %= mod
print(ans)
