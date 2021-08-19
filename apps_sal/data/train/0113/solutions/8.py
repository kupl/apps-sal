def ii():
    return int(input())


def si():
    return input()


def mi():
    return list(map(int, input().strip().split(' ')))


def li():
    return list(mi())


mod = 1000000000.0
t = ii()
while t:
    t -= 1
    (a, b) = mi()
    x = abs(b - a)
    c = x // 5
    x = x % 5
    c += x // 2
    x %= 2
    c += x
    print(c)
