import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def nextidx(h, x, y, dir):
    if y == h - 1 and dir == -1:
        return x + 1, y, 1
    elif y == 0 and dir == 1:
        return x + 1, y, -1
    else:
        return x, y - dir, dir


def main():
    h, w = nm()
    n = ni()
    A = nl()
    M = [[0] * w for _ in range(h)]
    dir = -1
    x = 0
    y = 0
    for i in range(n):
        for j in range(A[i]):
            M[x][y] = i + 1
            y, x, dir = nextidx(h, y, x, dir)
    for m in M:
        print((*m))


def __starting_point():
    main()


__starting_point()
