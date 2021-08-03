r, D, x = map(int, input().split())


def f(r, D, x):
    return r * x - D


for i in range(10):
    x = f(r, D, x)
    print(x)
