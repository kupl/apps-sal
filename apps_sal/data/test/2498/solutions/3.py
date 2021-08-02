import numpy as np
import sys


def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A_double = list([x // 2 for x in A])

    mini_multi = int(np.lcm.reduce(A_double))

    res = M // mini_multi

    for i in A_double:
        if (mini_multi // i) % 2 == 0:
            print((0))
            return

    if res % 2 != 0:
        res += 1

    print((res // 2))


def __starting_point():
    main()


__starting_point()
