# E
n = int(input())
c = [int(i) for i in input().split()]
mod = 10**9 + 7

c.sort()
ans = 0
for i in range(n):
    ans += c[i] * (n - i + 1)

ans %= mod
ans *= 4**(n - 1)
ans %= mod
print(ans)
