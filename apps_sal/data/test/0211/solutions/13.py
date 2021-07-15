MOD = 1000000009
def p2(e):
    if e == 0:
        return 1
    elif e % 2 == 1:
        return 2 * p2(e - 1) % MOD
    else:
        return p2(e // 2) ** 2 % MOD

n, m, k = map(int, input().split())
x = (m - min(n - m, m // (k - 1)) * (k - 1)) // k
print((2 * k * (p2(x) - 1) + m - x * k) % MOD)
