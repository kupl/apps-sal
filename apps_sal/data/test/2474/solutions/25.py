mod = 10 ** 9 + 7
n = int(input())
c = list(map(int, input().split()))
c.sort(reverse=True)
ans = 0
for i in range(n):
    ans += c[i] * (i + 2)
    ans %= mod
ans *= pow(4, n - 1, mod)
ans %= mod
print(ans)
