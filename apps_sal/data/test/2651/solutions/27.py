(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7
H = 0
W = 0
for i in range(n // 2):
    w = x[n - 1 - i] - x[i]
    if i == n // 2 - 1:
        if n % 2 == 1:
            w *= 2
    else:
        w *= n - 2 * i - 1
    W += w
    W %= mod
for j in range(m // 2):
    h = y[m - 1 - j] - y[j]
    if j == m // 2 - 1:
        if m % 2 == 1:
            h *= 2
    else:
        h *= m - 1 - 2 * j
    H += h
    H %= mod
S = H * W
print(S % mod)
