import numpy as np
import sys
input = sys.stdin.readline


def main():
    (n, k) = list(map(int, input().split()))
    A = np.array(sorted(list(map(int, input().split()))))
    F = np.array(sorted(list(map(int, input().split())), reverse=True))

    def is_time(x):
        c = np.maximum(A - x // F, 0).sum()
        if c <= k:
            return True
        return False
    ng = -1
    ok = max(A * F)
    while ok - ng > 1:
        m = (ng + ok) // 2
        if is_time(m):
            ok = m
        else:
            ng = m
    print(ok)


def __starting_point():
    main()


__starting_point()
