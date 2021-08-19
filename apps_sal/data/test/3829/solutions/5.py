(m, n) = list(map(int, input().split()))


def f(x):
    return (x / m) ** n


print('{:.9}'.format(sum(((f(i + 1) - f(i)) * (i + 1) for i in range(m)))))
