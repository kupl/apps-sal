import sys
import numpy as np
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    engine = np.zeros((n, 3))
    for i in range(n):
        (engine[i][0], engine[i][1]) = map(int, input().split())
        engine[i][2] = math.atan2(engine[i][1], engine[i][0])
    engines = engine[np.argsort(engine[:, 2])]
    sumen = sum(engines)
    ans = sumen[0] ** 2 + sumen[1] ** 2
    for i in range(n):
        for j in range(i, n):
            sump = sum(engines[i:j + 1])
            ans = max(ans, sump[0] ** 2 + sump[1] ** 2, (sump[0] - sumen[0]) ** 2 + (sump[1] - sumen[1]) ** 2)
    print(math.sqrt(ans))


def __starting_point():
    main()


__starting_point()
