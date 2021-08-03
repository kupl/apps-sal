import sys
import math
3


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, A):
    A.sort(reverse=True)

    lh = A[0]
    cnt = 1
    for a in A[1:]:
        if lh == 1:
            cnt += 1
        elif lh - 1 <= a:
            cnt += 1
            lh -= 1
        else:
            cnt += lh - a
            lh = a

    cnt += lh - 1

    return sum(A) - cnt


def main():
    N, M = [int(e) for e in inp().split()]
    A = [int(e) for e in inp().split()]
    assert len(A) == N
    print(solve(N, M, A))


def __starting_point():
    main()


__starting_point()
