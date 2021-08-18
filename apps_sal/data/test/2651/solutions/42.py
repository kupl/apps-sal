n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10**9 + 7
ans, ans2 = 0, 0
for i in range(n):
    ans = (ans + (-n + 2 * i + 1) * x[i]) % mod
for i in range(m):
    ans2 = (ans2 + (-m + 2 * i + 1) * y[i]) % mod
print(ans * ans2 % mod)
