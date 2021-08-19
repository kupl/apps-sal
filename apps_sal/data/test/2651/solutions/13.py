(n, m) = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10 ** 9 + 7
ans1 = 0
for k in range(1, n + 1):
    ans1 += (2 * k - 1 - n) * X[k - 1]
    ans1 %= mod
ans2 = 0
for k in range(1, m + 1):
    ans2 += (2 * k - 1 - m) * Y[k - 1]
    ans2 %= mod
print(ans1 * ans2 % mod)
