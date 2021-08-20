def f(n):
    if n in d:
        return d[n]
    d[n] = f(n // 2) + f((n - 1) // 2) + f((n - 2) // 2)
    return d[n]


d = {0: 1, 1: 2}
print(f(int(input())) % (10 ** 9 + 7))
