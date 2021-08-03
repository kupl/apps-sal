n = int(input().split()[0])
ps = []
for i in range(n):
    a, b = [int(x) for x in input().split()[:2]]
    ps.append([a, b])


def aline(a, b, c):
    x1 = a[1] - b[1]
    x2 = c[1] - b[1]
    y1 = a[0] - b[0]
    y2 = c[0] - b[0]
    if x1 * y2 == x2 * y1:
        return True
    else:
        return False


def left_fun(a, b, l):
    if len(l) < 3:
        return []
    to = [i for i in range(len(l)) if i != a and i != b]
    left = []
    for i in to:
        if not aline(ps[l[a]], ps[l[b]], ps[l[i]]):
            left.append(i)
    return left


def nm():
    if len(ps) < 5:
        print('YES')
        return
    l = [i for i in range(n)]
    left = left_fun(0, 1, l)
    left = left_fun(0, 1, left)
    if len(left) == 0:
        print('YES')
        return

    l = [i for i in range(n)]
    left = left_fun(1, 2, l)
    left = left_fun(0, 1, left)
    if len(left) == 0:
        print('YES')
        return

    l = [i for i in range(n)]
    left = left_fun(0, 2, l)
    left = left_fun(0, 1, left)
    if len(left) == 0:
        print('YES')
        return
    print('NO')


nm()
