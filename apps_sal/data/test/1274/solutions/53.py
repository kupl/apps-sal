import heapq
n, m = map(int, input().split())
t = [[] for _ in range(m + 1)]
for i in range(n):
    a, b = map(int, input().split())
    if a > m:
        continue
    t[a].append(b)
ans = 0
h = []
for l in t:
    for i in l:
        heapq.heappush(h, -i)
    if h:
        ans -= heapq.heappop(h)
print(ans)
