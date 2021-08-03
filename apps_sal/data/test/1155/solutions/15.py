def gis():
    return list(map(int, input().strip().split()))


def gi():
    return int(input())


def gss():
    return input().strip().split()


def problem():
    n, m = gis()
    maxi = 100
    for i in range(n):
        a, b = gis()
        maxi = min(maxi, a / b)
    print(maxi * m)


def __starting_point():
    problem()


__starting_point()
