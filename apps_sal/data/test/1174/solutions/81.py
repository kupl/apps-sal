import sys
stdin = sys.stdin

n,m = map(int, stdin.readline().split())
an = [i*(-1) for i in map(int, stdin.readline().split())]
#print(an)
#print(sum(an))

import heapq
heapq.heapify(an)

for _ in range(m):
    b = heapq.heappop(an)
    heapq.heappush(an, (-1)*((-1)*b//2))

#print(an)
ans = (-1)*sum(an)
print(ans)
