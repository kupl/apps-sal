def gis():
    return list(map(int, input().strip().split()))


def gi():
    return int(input())


def gss():
    return input().strip().split()


def problem():
    (n, m) = gis()
    ip = dict()
    for i in range(n):
        (name, ips) = gss()
        ip[ips] = name
    for i in range(m):
        (command, ips) = gss()
        print(command, ips, '#{}'.format(ip[ips[:-1]]))


def __starting_point():
    problem()


__starting_point()
