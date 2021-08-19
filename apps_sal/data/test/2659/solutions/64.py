def f(x):
    return x / sum(map(int, str(x)))


K = int(input())
(x, y) = (1, 1)
for i in range(K):
    print(x)
    if f(x + y) > f(x + y * 10):
        y *= 10
    x += y
