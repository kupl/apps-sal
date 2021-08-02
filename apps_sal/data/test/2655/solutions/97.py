import heapq as hq

n = int(input())
a = [int(_) for _ in input().split()]

a.sort()
p = a.pop()
q = []
hq.heappush(q, (-p, -p))
ans = 0
for _ in range(n - 1):
    p = a.pop()
    b1, b2 = hq.heappop(q)
    ans += -b1
    hq.heappush(q, sorted((b1, -p), reverse=True))
    hq.heappush(q, sorted((b2, -p), reverse=True))
print(ans)
