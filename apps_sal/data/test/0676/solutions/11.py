
n = int(input())

ar = [int(input()) for x in range(n)]

ar.sort()

foobar = 1


def out(*g):
    g = list(g)
    g.sort()
    print("YES")
    for x in g:
        print(x)


def check(x1, x2, x3, x4):
    l = [x1, x2, x3, x4]
    s = sum(l) / 4
    if s != int(s):
        return False
    l.sort()
    m = (l[1] + l[2]) / 2
    if m != int(m):
        return False
    d = l[3] - l[0]

    if not (s == m == d):
        return False
    return True


def _0():
    print('YES')
    print(1)
    print(1)
    print(3)
    print(3)


def _1():
    x = ar[0]
    print("YES")
    print(x)
    print(3 * x)
    print(3 * x)


def _2():
    x, y = ar
    if x * 3 < y:
        print("NO")
    else:

        print('YES')
        print(4 * x - y)
        print(3 * x)


def _3():
    x = ar[0]
    y = ar[1]
    z = ar[2]
    if x * 3 < z:
        print("NO")
    else:
        print('YES')
        print(3 * x)


def _3():
    ar.sort()
    m = (max(ar) + 10) * 10
    for x in range(1, m):
        if check(x, *ar):
            out(x)
            return

    print("NO")


def _4():
    r = check(*ar)
    if r == False:
        print('NO')
    else:
        print("YES")


vars()['_' + str(n)]()
