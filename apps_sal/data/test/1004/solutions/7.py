import sys
import os
3


def main():
    N = read_int()
    A = read_ints()
    ans = solve(N, A)
    if not ans:
        print('-1')
    else:
        print(len(ans))
        print(*ans)


def solve(N, A):
    ans = []

    start = 0
    present = set()
    left = set()
    for i, a in enumerate(A):
        if a > 0:
            if a in present or a in left:
                return None
            present.add(a)
        else:
            a = -a
            if a not in present:
                return None
            present.remove(a)
            left.add(a)

            if not present:
                ans.append(i - start + 1)
                start = i + 1
                left = set()

    if start != N:
        return None
    return ans


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()


__starting_point()
