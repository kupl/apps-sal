from operator import itemgetter
from collections import defaultdict
import heapq

n, m = list(map(int, input().split()))


d = defaultdict(list)
for i in range(n):
    a, b = list(map(int, input().split()))
    d[a].append(-b)
# l = sorted(l, key=itemgetter(1))
# l = l[::-1]
# print(d)
Q = []
heapq.heapify(Q)

ans = 0
for i in range(1, m + 1):
    for j in d[i]:
        heapq.heappush(Q, j)

    if Q:
        ans += -heapq.heappop(Q)
    # print(ans,i)
print(ans)
