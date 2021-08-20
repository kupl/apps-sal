import heapq
from collections import deque
from functools import lru_cache
(N, K) = list(map(int, input().split()))
V = list(map(int, input().split()))
ans = 0
for l in range(0, K + 1):
    for r in range(0, K - l + 1):
        d = K - r - l
        tmp = 0
        have = []
        if l + r > N:
            continue
        for i in range(0, l):
            tmp += V[i]
            have.append(V[i])
        for j in range(N - r, N):
            tmp += V[j]
            have.append(V[j])
        h = len(have)
        have = sorted(have)
        for k in range(0, d):
            if k >= h:
                break
            if have[k] > 0:
                break
            tmp -= have[k]
        ans = max(tmp, ans)
print(ans)
