import numpy as np
import math
import itertools
import sys
input = sys.stdin.readline


def main():
    numbers = []
    (n, m) = map(int, input().split())
    numbers = np.array([list(map(int, input().split())) for _ in range(n)])
    ans = 0
    length = 0
    count = 0
    for (idx, pair) in enumerate(itertools.combinations(numbers, 2)):
        tmp_A = np.array(pair[0])
        tmp_B = np.array(pair[1])
        length = (tmp_A - tmp_B) ** 2
        ans = math.sqrt(sum(length))
        if ans.is_integer() == True:
            count += 1
        else:
            continue
    print(count)


def __starting_point():
    main()


__starting_point()
