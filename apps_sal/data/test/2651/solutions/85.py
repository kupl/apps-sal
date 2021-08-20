(n, m) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10 ** 9 + 7
ans = 0
temp1 = 0
temp2 = 0
for i in range(n):
    temp1 += i * x[i] - (n - (i + 1)) * x[i]
    temp1 %= MOD
for i in range(m):
    temp2 += i * y[i] - (m - (i + 1)) * y[i]
    temp2 %= MOD
ans = temp1 * temp2
ans %= MOD
print(ans)
