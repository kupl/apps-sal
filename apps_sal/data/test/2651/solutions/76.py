n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
# ブロックの数は(m-1)*(n-1)
mod = pow(10, 9) + 7
ypoint = 0
for i in range(m - 1):
    ypoint += (y[i + 1] - y[i]) * (m - i - 1) * (i + 1)
    ypoint %= mod
ans = 0
for i in range(n - 1):
    ans += ypoint * (x[i + 1] - x[i]) * (n - i - 1) * (i + 1)
    ans %= mod
print(ans)
