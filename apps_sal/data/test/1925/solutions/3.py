(a, b, n) = list(map(int, input().split()))


def f(a, b, x):
    return a * x // b - a * (x // b)


print(f(a, b, min(b - 1, n)))
