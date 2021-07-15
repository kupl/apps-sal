n = int(input())
c = list(map(int, input().split()))
mod = 10 ** 9 + 7

c.sort(reverse=True)
ans = 0
for i, e in enumerate(c):
    ans += e * (2 + i)
    ans %= mod

ans *= pow(2, 2 * n - 2, mod)
ans %= mod

print(ans)

