from collections import deque
import heapq
n, k = map(int, input().split())
v = deque(list(map(int, input().split())))

ans = 0
for i in range(min(n, k) + 1):
    for j in range(min(n, k) - i + 1):
        l = [0]
        r = [0]
        mm = [0]
        for p in range(i):
            if v[p] > 0:
                l.append(v[p])
            else:
                heapq.heappush(mm, v[p])
        for o in range(j):
            if v[-o - 1] > 0:
                r.append(v[-o - 1])
            else:
                heapq.heappush(mm, v[-o - 1])
        for m in range(min(k - i - j, len(mm))):
            heapq.heappop(mm)
        ans = max(ans, sum(l) + sum(r) + sum(mm))
print(ans)
