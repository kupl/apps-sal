def ex_euclid(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    z0, z1 = a, b

    while z1 != 0:
        q = z0 // z1
        z0, z1 = z1, z0 % z1
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return z0, x0, y0


def mod_inv(a, n):
    g, x, _ = ex_euclid(a, n)
    if g != 1:
        print("modular inverse does not exist")
    else:
        return x % n


def mod_factorial(x, modulo):
    ans = 1
    for i in range(1, x + 1):
        ans *= i
        ans %= modulo
    return ans


X, Y = map(int, input().split())
M = 10 ** 9 + 7
a, b = (2 * X - Y) / 3, (2 * Y - X) / 3
if a < 0 or b < 0:
    print(0)
elif a == 0 and b == 0:
    print(0)
elif a % 1 != 0 or b % 1 != 0:
    print(0)
else:
    a, b = int(a), int(b)
    answer = 1
    answer *= mod_factorial(a + b, M)
    answer *= mod_inv(mod_factorial(a, M), M)
    answer %= M
    answer *= mod_inv(mod_factorial(b, M), M)
    answer %= M
    print(answer)
