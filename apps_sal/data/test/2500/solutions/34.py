N = int(input())

d = {0: 1, 1: 2}


def f(n):
    if n in d:
        return d[n]
    d[n] = (f(n // 2) + f((n - 1) // 2) + f((n - 2) // 2)) % (10**9 + 7)
    return d[n]


print(f(N))
