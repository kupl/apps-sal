(m, n) = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 1000000007
sum_x = 0
sum_y = 0
for k in range(m):
    sum_x += (2 * k + 1 - m) * X[k]
sum_x %= MOD
for l in range(n):
    sum_y += (2 * l + 1 - n) * Y[l]
sum_y %= MOD
Answer = sum_x * sum_y % MOD
print(Answer)
