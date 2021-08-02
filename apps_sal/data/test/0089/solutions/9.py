n = int(input())


def f(x):
    if x == 1:
        return 1
    if x % 2:
        return f(x - 1) + (x + 1) // 2
    return f(x - 1) + x // 2


print(f(n))
