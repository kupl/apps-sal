from collections import defaultdict
import sys
input = sys.stdin.buffer.readline


con = 10 ** 9 + 7


def getlist():
    return list(map(int, input().split()))


def main():
    N = int(input())
    A = getlist()
    M = max(A)
    p = A.index(M)
    m = min(A)
    q = A.index(m)
    if m >= 0:
        print(N - 1)
        for i in range(N - 1):
            print(i + 1, i + 2)
    else:
        if abs(M) > abs(m):
            print(2 * N - 1)
            for i in range(N):
                print(p + 1, i + 1)
            for i in range(N - 1):
                print(i + 1, i + 2)
        else:
            print(2 * N - 1)
            for i in range(N):
                print(q + 1, i + 1)
            for i in range(N - 1):
                print(N - i, N - 1 - i)


def __starting_point():
    main()


__starting_point()
