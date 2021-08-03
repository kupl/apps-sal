MOD = 10**9 + 7

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_dif = [b - a for a, b in zip(x, x[1:])]
y_dif = [b - a for a, b in zip(y, y[1:])]


def cumd(dif, line):
    d_sum = 0
    for i, d in enumerate(dif, 1):
        d_sum += d * i * (line - i) % MOD
        d_sum %= MOD
    return d_sum


dx_sum = cumd(x_dif, n)
dy_sum = cumd(y_dif, m)


print(dx_sum * dy_sum % MOD)
