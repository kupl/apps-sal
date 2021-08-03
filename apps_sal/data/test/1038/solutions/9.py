A, B = map(int, input().split())


def f(X):
    a, b = divmod(X + 1, 2)
    return (a % 2) ^ (X * b)


print(f(max(0, A - 1)) ^ f(B))
