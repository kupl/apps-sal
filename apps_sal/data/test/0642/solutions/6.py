import sys


def check_stairs(n, stairs):
    if len(stairs) == 0:
        print('YES')
        return
    if stairs[0] == 1 or stairs[-1] == n:
        print('NO')
        return
    for i in range(len(stairs) - 2):
        if stairs[i] + 1 == stairs[i + 1] and stairs[i] + 2 == stairs[i + 2]:
            print('NO')
            return
    print('YES')


def __starting_point():

    nm_list = [int(c) for c in sys.stdin.readline().rstrip().split(' ')]
    (n, m) = tuple(nm_list)
    stairs = []
    if m > 0:
        stairs = [int(c) for c in sys.stdin.readline().rstrip().split(' ')]
        stairs.sort()
    check_stairs(n, stairs)


__starting_point()
