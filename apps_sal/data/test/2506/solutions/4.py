import numpy as np
import sys
input = sys.stdin.readline


def main():
    (N, M) = list(map(int, input().split()))
    A = np.array(sorted([int(i) for i in input().split()]))
    left = 0
    right = A[-1] * 2 + 5
    while right - left > 1:
        x = (left + right) // 2
        count = N ** 2 - np.searchsorted(A, x - A).sum()
        if count >= M:
            left = x
        else:
            right = x
    bound = np.searchsorted(A, left - A)
    count = N ** 2 - bound.sum()
    diff = count - M
    ans = ((N - bound) * A * 2).sum() - diff * left
    print(ans)


def __starting_point():
    main()


__starting_point()
