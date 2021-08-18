import sys
import os
3


def main():
    A, B, C, D = read_ints()
    ans = solve(A, B, C, D)
    if ans:
        print('YES')
        print(*ans)
    else:
        print('NO')


def solve(A, B, C, D):
    S = A + B + C + D
    for l in range(4):
        for r in range(4):
            ans = build([A, B, C, D], S, l, r)
            if ans:
                return ans

    return None


def build(A, S, l, r):
    if A[l] == 0:
        return None
    ans = [l]
    A[l] -= 1
    i = l
    S -= 1
    while S > 0:
        if i == 0:
            j = 1
        elif i == 1:
            if A[0] == 0:
                j = 2
            elif A[2] == 0:
                j = 0
            elif r <= 1:
                j = 2
            else:
                j = 0
        elif i == 2:
            if A[3] == 0:
                j = 1
            elif A[1] == 0:
                j = 3
            elif r >= 2:
                j = 1
            else:
                j = 3
        else:
            j = 2

        A[j] -= 1
        S -= 1
        ans.append(j)
        if A[j] < 0:
            return None
        i = j

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
