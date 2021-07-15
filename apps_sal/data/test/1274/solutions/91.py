import collections
import heapq

n, m = map(int, input().split())
que = []
for _ in range(n):
    a, b = map(int, input().split())
    que.append((-b, a))
que.sort(key=lambda x: x[1])
que = collections.deque(que)
h = []
heapq.heapify(h)
ans = 0
for i in range(1, m + 1):
    while len(que) != 0 and que[0][1] <= i:
        tmp = que.popleft()
        heapq.heappush(h, tmp)
    if len(h) == 0: continue
    tmp = heapq.heappop(h)
    ans -= tmp[0]
print(ans)
