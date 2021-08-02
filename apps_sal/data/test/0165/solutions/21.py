def f(a, b, c):
    m = min(a, b, c)
    a, b, c = a - m, b - m, c - m
    if a == b and a == c: return 0
    if a == b:
        if abs(a - c) == 1: return 0
        elif c > a: return (c - a - 1) * 2
        else: return a - c - 1
    if a == c:
        if abs(a - b) == 1: return 0
        elif b > a: return (b - a - 1) * 2
        else: return a - b - 1
    if b == c:
        if abs(a - b) == 1: return 0
        elif a > b: return (a - b - 1) * 2
        else: return b - a - 1

    m = min(a, b, c)
    n = min(max(a, b), max(b, c), max(a, c))
    if a == m: a = n
    elif b == m: b = n
    else: c = n
    return n + f(a, b, c)


print(f(*[int(i) for i in input().split()]))
