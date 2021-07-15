mod = 998244353
n = int(input())
d = list(map(int, input().split()))
s = sum(d) % mod
ans = 1
for i in d:
    ans *= i
    ans %= mod
for i in range(n, 2 * n - 2):
    ans *= (s - i)
    ans %= mod
print(ans)
