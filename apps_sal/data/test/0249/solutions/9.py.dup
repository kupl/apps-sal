n, l, x, y = map(int, input().split())
s = set(map(int, input().split()))


def f(d): return any(i + d in s for i in s)


def g():
    for i in s:
        if i + x + y in s:
            return i + x
    return 0


def h():
    for i in s:
        if i + y - x in s:
            if i - x >= 0:
                return i - x
            if i + y <= l:
                return i + y
    return 0


def e(d):
    print(1)
    print(d)


if f(x):
    if f(y):
        print(0)
    else:
        e(y)
elif f(y):
    e(x)
else:
    z = g()
    if z:
        e(z)
    else:
        z = h()
        if z:
            e(z)
        else:
            print(2)
            print(x, y)
