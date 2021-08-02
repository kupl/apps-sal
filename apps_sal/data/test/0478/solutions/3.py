import sys
import math
import bisect


def solve(A):
    n = len(A)
    for i in range(25, -1, -1):
        to_loop = True
        while to_loop:
            to_loop = False
            for j in range(len(A)):
                #print('A: %s, j: %d' % (str(A), j))
                if A[j] == i and j - 1 >= 0 and A[j - 1] == i - 1:
                    A = A[0:j] + A[j + 1:]
                    to_loop = True
                    break
                elif A[j] == i and j + 1 < len(A) and A[j + 1] == i - 1:
                    A = A[0:j] + A[j + 1:]
                    to_loop = True
                    break
    return n - len(A)


def main():
    n = int(input())
    A = list(input())
    for i in range(n):
        A[i] = ord(A[i]) - ord('a')
    ans = solve(A)
    print(ans)


def __starting_point():
    main()


__starting_point()
