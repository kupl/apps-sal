n, l, x, y = map(int, input().split())


def f(t, q):
    i = j = 0
    while j < n:
        d = t[j] - t[i]
        if d < q:
            j += 1
        elif d > q:
            i += 1
        else:
            return 0
    return q


def g(t):
    q = x + y
    i = j = 0
    while j < n:
        d = t[j] - t[i]
        if d < q:
            j += 1
        elif d > q:
            i += 1
        else:
            return t[j]
    return 0


def h(t):
    q = y - x
    i = j = 0
    while j < n:
        d = t[j] - t[i]
        if d < q:
            j += 1
        elif d > q:
            i += 1
        else:
            a, b = t[i] - x, t[j] + x
            if a >= 0:
                return [a]
            if b <= l:
                return [b]
            j += 1
    return [x, y]


def e(t):
    print(len(t))
    print(' '.join(map(str, t)))


t = list(map(int, input().split()))
t.sort()
x = f(t, x)
y = f(t, y)
if x and y:
    z = g(t)
    if z:
        e([z - y])
    else:
        e(h(t))
elif x:
    e([x])
elif y:
    e([y])
else:
    e([])
