def prm(a, b):
    ld = (min(a[0], b[0]), min(a[1], b[1]))
    ru = (max(a[0], b[0]), max(a[1], b[1]))
    return tuple((ld, ru))


def peres(a, b):
    return tuple(((max(a[0][0], b[0][0]), max(a[0][1], b[0][1])), (min(a[1][0], b[1][0]), min(a[1][1], b[1][1]))))


def rst(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + 1


def printt(a):
    nonlocal h
    if h != a:
        print(*a)
    s1 = set([])
    for i in range(min(a[0], h[0]), max(a[0], h[0]) + 1):
        j = h[1]
        if ((i, j) != h) and ((i, j) != a):
            print(i, j)
            s1.add((i, j))
    for j in range(min(a[1], h[1]), max(a[1], h[1]) + 1):
        i = a[0]
        if ((i, j) != h) and ((i, j) != a) and (i, j) not in s1:
            print(i, j)


a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
h = peres(peres(prm(a, b), prm(a, c)), prm(b, c))[0]
print(rst(a, h) + rst(b, h) + rst(c, h) - 2)
printt(a)
printt(b)
printt(c)
print(*h)
