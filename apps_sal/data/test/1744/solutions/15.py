import itertools
from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
t = list(map(int, input().split()))
tsum = list(itertools.accumulate(t))
ans = []
for i in range(n):
    if tsum[i] <= m:
        ans.append(0)
    else:
        heap = [-k for k in t[:i]]
        heapify(heap)
        remain = sum(t[:i]) - m
        count = 0
        for j in range(i, n):
            uselist = []
            remain += t[j]
            while remain > 0:
                count += 1
                use = heappop(heap)
                remain += use
                uselist.append(use)
            else:
                ans.append(count)
                uselist.sort(reverse=True)
            summ = 0
            for uses in uselist[:100]:
                heappush(heap, uses)
                remain -= uses
                summ -= uses
                count -= 1
                if summ > 100:
                    break
            heappush(heap, -t[j])
        break
print(' '.join(map(str, ans)))
