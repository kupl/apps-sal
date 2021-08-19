m = 10 ** 9 + 7


def f(r, c):
    s = t = 1
    for i in range(c):
        s = s * (r + c - i) % m
        t = t * -~i % m
    return s * pow(t, m - 2, m) % m


(a, b, c, d) = map(int, input().split())
print((f(a, b) - f(c + 1, b) - f(a, d + 1) + f(c + 1, d + 1)) % m)
