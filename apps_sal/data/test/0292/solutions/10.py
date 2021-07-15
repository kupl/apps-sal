__author__ = 'Konrad Strack'


def command_gen():
    while True:
        yield 'L'
        yield 'R'


def solve():
    h, n = [int(x) for x in input().split()]

    leaves = 2 ** h

    path = []
    left, right = 1, leaves
    for i in range(h):
        middle = (left + right) // 2
        if n <= middle:
            path.append('L')
            right = middle
        else:
            path.append('R')
            left = middle + 1

    command = command_gen()
    sum = 0
    hi = h
    for p in path:
        cmd = next(command)

        if p != cmd:
            sum += 2 ** hi - 1
            next(command)
        hi -= 1

    sum += len(path)
    print(sum)


def __starting_point():
    solve()
__starting_point()
