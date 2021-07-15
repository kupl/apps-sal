######################
# AC: ms(PyPy)
# AC: ms(Python3)
######################

from bisect import bisect_left
import sys
input = sys.stdin.readline


def main():
    N,M = list(map(int, input().split()))
    A = [int(i) for i in input().split()]

    A.sort()

    left = 0
    right = A[-1] * 2 + 5
    while right - left > 1:
        X = (left + right) // 2

        count = 0
        for a in A:
            i = bisect_left(A, X-a)
            count += (N - i)

        if count >= M:
            left = X
        else:
            right = X

    count = 0
    num = []
    append = num.append
    for a in A:
        i = bisect_left(A, left-a)
        count += (N - i)
        append(N - i)

    diff = count - M
    ans = 0
    for i, a in zip(num, A):
        ans += i * a

    print((ans * 2 - diff * left))


def __starting_point():
    main()

__starting_point()
