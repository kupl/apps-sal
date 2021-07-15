#!/usr/bin/env python3
import numpy as np


def is_ok(mid, K, A, F):
    return np.maximum(A - mid // F, 0).sum() <= K


def main():
    N, K = input_line(int, int)
    A = input_line([int])
    F = input_line([int])
    A = np.array(sorted(A))
    F = np.array(sorted(F, reverse=True))

    ng = -1
    ok = int(1e12)
    while ok - ng > 1:
        mid = (ng + ok) // 2
        if is_ok(mid, K, A, F):
            ok = mid
        else:
            ng = mid
    print(ok)


def input_line(*types):
    if isinstance(types[0], list):
        return [types[0][0](x) for x in input().split()]
    elif len(types) == 1:
        return types[0](input())
    else:
        return [t(x) for t, x in zip(types, input().split())]


def __starting_point():
    main()

__starting_point()
