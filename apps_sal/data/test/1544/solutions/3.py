n = int(input())


def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def c(n, k):
    return fact(n) // (fact(k) * fact(n - k))


def f(n, x):
    return c(x + n - 1, n - 1)


print(f(n, 3) * f(n, 5))
