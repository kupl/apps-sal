from collections import defaultdict
import sys


def __starting_point():
    n = int(input())
    index = list(map(int, input().split()))
    index.sort()
    print(index[(n - 1) // 2])


__starting_point()
