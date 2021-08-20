import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
N = int(input())
S = input()
ans = ['S'] * N


def ok(ST):
    ret = ['S'] * N
    ret[-1] = ST[-1]
    ret[0] = ST[0]
    for i in range(0, N - 2):
        if ret[i] == 'S':
            if S[i] == 'o':
                ret[i + 1] = ret[i - 1]
            else:
                ret[i + 1] = 'W' if ret[i - 1] == 'S' else 'S'
        elif S[i] == 'o':
            ret[i + 1] = 'W' if ret[i - 1] == 'S' else 'S'
        else:
            ret[i + 1] = ret[i - 1]
    for i in range(N):
        if S[i] == 'o' and ret[i] == 'S' and (ret[i - 1] != ret[(i + 1) % N]):
            return False
        if S[i] == 'o' and ret[i] == 'W' and (ret[i - 1] == ret[(i + 1) % N]):
            return False
        if S[i] == 'x' and ret[i] == 'S' and (ret[i - 1] == ret[(i + 1) % N]):
            return False
        if S[i] == 'x' and ret[i] == 'W' and (ret[i - 1] != ret[(i + 1) % N]):
            return False
    return ''.join(ret)


def solve():
    for s in ['SS', 'SW', 'WS', 'WW']:
        r = ok(s)
        if r:
            print(r)
            return
    print(-1)


solve()
