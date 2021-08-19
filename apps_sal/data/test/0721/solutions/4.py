import sys


def __starting_point():
    (n, d) = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]
    a_arr = sorted([int(i) for i in sys.stdin.readline().rstrip().split(' ')])
    m = int(sys.stdin.readline().rstrip())
    if m <= n:
        print(sum(a_arr[:m]))
    else:
        print(sum(a_arr) - (m - n) * d)


__starting_point()
