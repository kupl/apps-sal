(a, b, n, x) = map(int, input().split())
md = 10 ** 9 + 7


def mult(u, v):
    return 0 if v == 0 else (u + mult(u, v - 1)) % md if v % 2 == 1 else 2 * mult(u, v // 2) % md


def get_prog(a, b, n):
    return mult(pow(a, n, md) - 1 + md, pow(a - 1 + md, md - 2, md)) if a != 1 else n


res = mult(pow(a, n, md), x) + mult(get_prog(a, b, n), b)
res %= md
print(res)
