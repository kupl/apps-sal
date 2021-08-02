mod = 10**9 + 7
n = int(input())
c = list(map(int, input().split()))
c.sort(reverse=True)

b = pow(2, 2 * n - 2, mod)
a = 2 * b % mod

ans = 0
for i in range(n):
    ans += c[i] * (a + i * b)
    ans %= mod

print(ans)
