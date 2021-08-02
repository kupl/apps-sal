def gis():
    return list(map(int, input().strip().split()))


def gi():
    return int(input())


def gss():
    return input().strip().split()


def problem():
    n = gi()
    f0 = 1
    f1 = 1
    f = set()
    while f0 <= n:
        f.add(f0)
        c = f0 + f1
        f0 = f1
        f1 = c
    name = ''
    for i in range(n):
        if (i + 1) in f:
            name += 'O'
        else:
            name += 'o'
    print(name)


def __starting_point():
    problem()


__starting_point()
