def f(l):
    n = len(l)
    if n == 1:
        return l[0]
    nn = pow(9, n - 1)
    res = nn
    for i in range(1, l[0]):
        res = max(res, i * nn)
    res = max(l[0] * f(l[1:]), res)
    return res


x = [*map(int, input())]
print(f(x))
