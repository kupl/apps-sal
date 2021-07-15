from math import gcd

from math import factorial as f

from math import ceil, floor, sqrt
import math

import bisect
import re
import heapq

from copy import deepcopy
import itertools
from itertools import permutations


ii = lambda: int(input())
mi = lambda: list(map(int, input().split()))
li = lambda: list(map(int, input().split()))

yes = "Yes"
no = "No"


def main():
    a, b = mi()
    print((100, 100))
    ans = [[] for i in range(100)]
    for i in range(50):
        for j in range(100):
            ans[i].append('#')
    for i in range(50, 100):
        for j in range(100):
            ans[i].append('.')

    for i in range(a - 1):
        ans[2 * (i // 50)][2 * (i % 50)] = '.'
    for i in range(b - 1):
        ans[99 - 2 * (i // 50)][2 * (i % 50)] = '#'

    for i in range(100):
        print((''.join(ans[i])))


main()

