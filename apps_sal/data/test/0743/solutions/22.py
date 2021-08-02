def g(x):
    if len(x) == 1:
        return x[0]
    if x[0] == 0:
        return g(x[1:])
    return g([x[-1] % x[0]] + x[:-1])


input()
a = list(map(int, input().split()))
print(g(a) * len(a))
