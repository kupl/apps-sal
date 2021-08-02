import heapq as h
n = int(input())
a = [int(x) for x in input().split()]
if len(a) % 2 == 0:
    a.append(0)
h.heapify(a)
ans = 0
while len(a) > 1:
    a1 = h.heappop(a)
    a2 = h.heappop(a)
    a3 = h.heappop(a)
    ans += a1 + a2 + a3
    h.heappush(a, a1 + a2 + a3)
print(ans)
