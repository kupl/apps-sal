from collections import defaultdict as df
import heapq
import bisect
import math
from itertools import combinations, permutations
from collections import deque

n, k = list(map(int, input().split()))
a = list(map(int, input().rstrip().split()))
ans = []
for i in a:
    if i in ans:
        pass
    else:
        if len(ans) >= k:
            ans.pop()
            ans.insert(0, i)
        else:
            ans.insert(0, i)
print(len(ans))
print(*ans)
