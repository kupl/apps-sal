import sys


def read_data():
    n, x0 = list(map(int, next(sys.stdin).split()))
    checkpoints = list(map(int, next(sys.stdin).split()))
    return x0, checkpoints


def solve(x0, checkpoints):
    n = len(checkpoints)
    checkpoints.sort()
    if n == 1:
        return 0
    case0 = abs(x0 - checkpoints[1]) + abs(checkpoints[n - 1] - checkpoints[1])
    case1 = abs(x0 - checkpoints[n - 2]) + abs(checkpoints[0] - checkpoints[n - 2])
    case2 = abs(x0 - checkpoints[0]) + abs(checkpoints[n - 2] - checkpoints[0])
    case3 = abs(x0 - checkpoints[n - 1]) + abs(checkpoints[1] - checkpoints[n - 1])
    return min(case0, case1, case2, case3)


def __starting_point():
    x0, checkpoints = read_data()
    length = solve(x0, checkpoints)
    print(length)


__starting_point()
