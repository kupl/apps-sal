(W, a, b) = map(int, input().split())


def f(x):
    return x if x > 0 else 0


print(f(abs(a - b) - W))
