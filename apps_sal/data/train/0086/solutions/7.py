from math import log2, ceil


def readGenerator():
    while True:
        tokens = input().split(' ')
        for t in tokens:
            yield t


reader = readGenerator()


def readWord():
    return next(reader)


def readInt():
    return int(next(reader))


def readFloat():
    return float(next(reader))


def readLine():
    return input()


def solve(a):
    v0, v1 = 0, 0
    for i in a:
        if i == 0:
            v0 += 1
        else:
            v1 += 1

    if v1 > v0:
        if v1 % 2 != 0:
            v1 -= 1
        print(v1)
        return '1 ' * v1
    print(v0)
    return '0 ' * v0


tests = readInt()

for i in range(tests):
    n = readInt()
    a = [readInt() for _ in range(n)]
    print(solve(a))
