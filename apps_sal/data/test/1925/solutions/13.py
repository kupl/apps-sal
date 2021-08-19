(A, B, N) = map(int, input().split())


def f(x):
    return int(A * x / B) - A * int(x / B)


print(f(min(B - 1, N)))
