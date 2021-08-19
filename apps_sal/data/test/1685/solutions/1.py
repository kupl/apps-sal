(n, q) = [int(i) for i in input().split()]


def identify_row(x):
    for i in range(1, 64):
        power = 1 << i
        if x % power == power >> 1:
            return i


def some(x):
    r = identify_row(x)
    return x - (1 << r - 1) + 1


def left(x):
    r = identify_row(x)
    if r == 1:
        return x
    return x - (1 << r - 2)


def right(x):
    r = identify_row(x)
    if r == 1:
        return x
    return x + (1 << r - 2)


def parent(x):
    if x == n + 1 >> 1:
        return x
    r = identify_row(x)
    return x + (1 << r - 1 if some(x) % (1 << r + 1) == 1 else -1 << r - 1)


for _ in range(q):
    t = int(input())
    c = input()
    for i in c:
        if i == 'U':
            t = parent(t)
        elif i == 'R':
            t = right(t)
        elif i == 'L':
            t = left(t)
        else:
            print('error', i)
    print(t)
