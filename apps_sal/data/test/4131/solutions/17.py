import sys
from collections import deque


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m = nm()
    Y = [deque() for _ in range(n)]
    Y_id = []
    order = []
    for i in range(m):
        p, y = nm()
        Y[p - 1].append(y)
        order.append(p)

    for y in Y:
        d = {}
        for i, y_s in enumerate(sorted(y)):
            d[y_s] = i + 1
        Y_id += [d]

    for o in order:
        print(('{:06}'.format(o) +
              '{:06}'.format(Y_id[o - 1][Y[o - 1].popleft()])))


def __starting_point():
    main()

__starting_point()
