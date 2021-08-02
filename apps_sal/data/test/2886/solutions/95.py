import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

S = input()
L = len(S)


def p():
    for j in range(L - 2):
        if S[j] == S[j + 1]:
            print(j + 1, j + 2)
            return
        if S[j] == S[j + 2]:
            print(j + 1, j + 3)
            return

    if S[-2] == S[-1]:
        print(L - 1, L)
    else:
        print(-1, -1)


p()
