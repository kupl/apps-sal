import collections
import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

K = int(input())


def ans():
    visited = [False] * K

    s = (1, 1)

    q = collections.deque()
    q.append(s)

    while True:
        c = q.popleft()
        visited[c[0]] = True

        if c[0] == 0:
            return c[1]

        if not visited[(c[0] * 10) % K] and not visited[(c[0] * 10) % K]:
            q.appendleft(((c[0] * 10) % K, c[1]))

        if not visited[(c[0] + 1) % K] and not visited[(c[0] + 1) % K]:
            q.append(((c[0] + 1) % K, c[1] + 1))


print((ans()))


