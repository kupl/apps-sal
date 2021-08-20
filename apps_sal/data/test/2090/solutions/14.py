from heapq import heappush, heappop
(n, k) = map(int, input().split())
a = []
for i in range(n):
    (x, y) = map(int, input().split())
    a.append([y, x])
a.sort(reverse=True)
h = []
ans = 0
sum_len = 0
for (b, t) in a:
    sum_len += t
    heappush(h, t)
    if len(h) > k:
        sum_len -= heappop(h)
    ans = max(ans, sum_len * b)
print(ans)
