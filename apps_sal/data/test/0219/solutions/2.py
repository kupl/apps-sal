import sys


def solve():
    (n, m, s, d) = [int(x) for x in input().split()]
    obstacles = [int(x) for x in input().split()]
    obstacles.sort()
    if obstacles[0] <= s:
        return False
    pieces = [[obstacles[0], obstacles[0]]]
    for x in obstacles:
        if pieces[-1][1] + s + 2 > x:
            pieces[-1][1] = x
        else:
            if pieces[-1][1] - pieces[-1][0] + 2 > d:
                return False
            pieces.append([x, x])
    if pieces[-1][1] - pieces[-1][0] + 2 > d:
        return False
    pos = 0
    for piece in pieces:
        sys.stdout.write('RUN ' + str(piece[0] - pos - 1) + '\n')
        sys.stdout.write('JUMP ' + str(piece[1] - piece[0] + 2) + '\n')
        pos = piece[1] + 1
    if pos < m:
        sys.stdout.write('RUN ' + str(m - pos) + '\n')
    return True


if not solve():
    print('IMPOSSIBLE')
