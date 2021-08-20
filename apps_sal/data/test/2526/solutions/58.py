import heapq
(x, y, a, b, c) = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = list(map(lambda x: -int(x), input().split()))
heapq.heapify(r)
for i in range(x):
    heapq.heappush(r, -p[i])
for i in range(y):
    heapq.heappush(r, -q[i])
ans = 0
for i in range(x + y):
    ans -= heapq.heappop(r)
print(ans)
