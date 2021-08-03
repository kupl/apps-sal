def f(a, b):
    if a == 0 or b == 0:
        return (a, b)
    if a >= 2 * b:
        return f(a % (2 * b), b)
    elif b >= 2 * a:
        return f(a, b % (2 * a))
    return (a, b)


a, b = map(int, input().split())
print(' '.join(list(map(str, f(a, b)))))
