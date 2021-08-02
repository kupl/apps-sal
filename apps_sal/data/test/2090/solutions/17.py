from heapq import heappush, heappop
n, k = map(int, input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([y, x])
a.sort(reverse=True)
h = []
ans, sm = 0, 0
for b, l in a:
    sm += l
    heappush(h, l)
    if len(h) > k:
        sm -= heappop(h)
    ans = max(ans, sm * b)
print(ans)
