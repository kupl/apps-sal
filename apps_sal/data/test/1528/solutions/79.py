(N, X) = map(int, input().split())


def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + 2 ** (N + 1) - 3:
        return f(N - 1, X - 1)
    else:
        return 2 ** N + f(N - 1, X - 2 ** (N + 1) + 3 - 2)


print(f(N, X))
