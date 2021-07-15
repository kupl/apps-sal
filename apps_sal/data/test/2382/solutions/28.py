from collections import Counter
from heapq import heapify, heappush, heappop

def solve():
    N = int(input())
    Ss = list(map(int, input().split()))

    cnt = Counter(Ss)

    PQ = [-N]
    for key in sorted(list(cnt.keys()), reverse=True):
        num = cnt[key]
        if len(PQ) < num:
            return False
        depths = []
        for _ in range(num):
            depths.append(-heappop(PQ))
        for depth in depths:
            for d in range(depth):
                heappush(PQ, -d)

    return True

if solve():
    print('Yes')
else:
    print('No')


