
def f(n):
    if n < 0:
        return 0
    val = ((n + 3) * (n + 2) * (n + 1)) // 6
    return val


def g(n):
    return f(n) - f(n - 6) - 2 * f(n - 9) + f(n - 10) + f(n - 14)


n = int(input())
print(g(n))
