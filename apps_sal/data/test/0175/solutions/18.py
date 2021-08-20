(a, b) = tuple(map(int, input().split()))


def step(a, b):
    if a == 0 or b == 0:
        n = 0
    elif a > b:
        n = a // (2 * b)
        a = a - n * 2 * b
    else:
        n = b // (2 * a)
        b -= n * 2 * a
    if n != 0:
        return step(a, b)
    return (a, b)


d = step(a, b)
print(d[0], d[1])
