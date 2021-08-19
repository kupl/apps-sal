H, W, A, B = list(map(int, input().split()))

# H行W列 左下から縦A横B


def mod(num):
    return num % (10 ** 9 + 7)


n = H + W + 1

fac = [0] * n
rev = [0] * n

fac[0] = 1

for i in range(1, n):
    fac[i] = mod(fac[i - 1] * i)


# 逆元の計算 x**(-1) ≡ x**(10**9 + 5) (mod 10**9 + 7)
rev[n - 1] = pow(fac[n - 1], 10**9 + 5, 10**9 + 7)

for i in range(n - 2, 0, -1):
    rev[i] = mod(rev[i + 1] * (i + 1))

rev[0] = 1

t1 = [0] * (W - B)

for i in range(W - B):
    t1[i] = mod(fac[H - A - 1 + i + B] * mod(rev[B + i] * rev[H - A - 1]))

res = 0

for i in range(W - B):
    r = t1[i] * mod(fac[A - 1 + W - B - 1 - i] * mod(rev[A - 1] * rev[W - B - 1 - i]))
    res = mod(res + r)

print(res)
