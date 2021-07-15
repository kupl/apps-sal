import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

X, Y, Z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
C = sorted(C, reverse=True)
i, j, k = 0, 0, 0
heap = [(-A[i] - B[j] - C[k], i, j, k)]
heapq.heapify(heap)
used_set = set([(i, j, k)])
for _ in range(K):
    oisi, i, j, k = heapq.heappop(heap)
    print((-oisi))
    if (i+1, j, k) in used_set:
        pass
    elif(i+1 < len(A)):
        used_set.add((i+1, j, k))
        heapq.heappush(heap, (-A[i+1]-B[j]-C[k], i+1, j, k))
    if (i, j+1, k) in used_set:
        pass
    elif(j+1 < len(B)):
        used_set.add((i, j+1, k))
        heapq.heappush(heap, (-A[i] - B[j+1] - C[k], i, j+1, k))
    if (i, j, k+1) in used_set:
        pass
    elif(k+1 < len(C)):
        used_set.add((i, j, k+1))
        heapq.heappush(heap, (-A[i]-B[j]-C[k+1], i, j, k+1))

