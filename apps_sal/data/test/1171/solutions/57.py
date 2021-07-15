import heapq
from collections import deque
n , k = map(int,input().split())
v = list(map(int,input().split()))
ans = 0
for i in range(n+1):
    for j in range(n+1):
        if i+j > n or i+j > k:
            continue
        p = v[:]
        d = deque(p)
        a = []
        heapq.heapify(a)
        for t in range(i):
            heapq.heappush(a,d.popleft())
        for l in range(j):
            heapq.heappush(a,d.pop())
        nokori = k-i-j
        for s in range(nokori):
            if a:
                now = heapq.heappop(a)
                if now > 0:
                    heapq.heappush(a,now)
                    break
            else:
                break
        ans = max(ans,sum(a))
print(ans)
