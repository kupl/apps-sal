(N, X) = map(int, input().split())


def A(x):
    return pow(2, x + 2) - 3


def P(x):
    return pow(2, x + 1) - 1


def f(n, x):
    if n == 0:
        return 1
    if n == 1:
        return min(x - 1, 3)
    if x <= n:
        return 0
    if A(n) // 2 + 1 == x:
        return P(n - 1) + 1
    if A(n) == x:
        return P(n)
    if A(n) // 2 >= x:
        return f(n - 1, x - 1)
    return P(n - 1) + 1 + f(n - 1, x - A(n) // 2 - 1)


print(f(N, X))
