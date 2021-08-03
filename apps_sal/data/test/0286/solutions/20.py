import queue


def readTuple():
    return input().split()


def readInts():
    return tuple(map(int, readTuple()))


def solve():
    n = int(input().strip())
    print(n // 2 + 1)


def __starting_point():
    solve()


__starting_point()
