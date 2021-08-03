import sys

import math
import numpy as np


def main():
    n = int(input())
    vec = [tuple(map(int, input().split())) for i in range(n)]
    vec.sort(key=lambda x: math.atan2(x[1], x[0]))

    maxx = 0
    for i in range(n):
        for j in range(1, n + 1):
            now = [0, 0]
            for k in range(j):
                idx = (i + k) % n
                now[0] += vec[idx][0]
                now[1] += vec[idx][1]
            maxx = max(maxx, now[0] * now[0] + now[1] * now[1])

    print((math.sqrt(maxx)))
    return 0


def __starting_point():
    return(main())


__starting_point()
