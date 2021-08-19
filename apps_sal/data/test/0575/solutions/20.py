import sys
next(sys.stdin)
(q_x, q_y) = list(map(int, next(sys.stdin).rstrip().split()))
(k_x, k_y) = list(map(int, next(sys.stdin).rstrip().split()))
(dest_x, dest_y) = list(map(int, next(sys.stdin).rstrip().split()))


def sign(x):
    return 1 if x >= 0 else -1


def which_square(x, y):
    return (sign(x - q_x), sign(y - q_y))


if which_square(k_x, k_y) == which_square(dest_x, dest_y):
    print('YES')
else:
    print('NO')
