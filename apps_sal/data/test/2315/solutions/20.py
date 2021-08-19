def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


for t in range(ii()):
    (l, r) = mi()
    print(l, 2 * l)
