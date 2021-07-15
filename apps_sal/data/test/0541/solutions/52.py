import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N, M = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(M)]
AB.sort()

q = []
for ab in AB:
    heapq.heappush(q, ab)

ans = 0
cnt = M
visited = -1
while cnt > 0:
    ab = heapq.heappop(q)
    cnt -= 1

    # print(ab, visited, cnt)

    if ab[1] > ab[0]:
        heapq.heappush(q, [ab[1], ab[0]])
        cnt += 1
    else:
        if visited <= ab[1]:
            visited = ab[0]
            ans += 1
        else:
            pass

print(ans)
