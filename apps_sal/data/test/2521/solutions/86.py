import heapq
n = int(input())
a = list(map(int, input().split()))
b = a[n:2 * n]


q = a[:n]
heapq.heapify(q)

res = [0] * (n + 1)
res[0] = sum(q)
for i, x in enumerate(b):
    heapq.heappush(q, x)
    y = heapq.heappop(q)
    res[i + 1] = res[i] + x - y

b.reverse()
q = [-x for x in a[2 * n:]]
heapq.heapify(q)
s = -sum(q)
res[-1] -= s

for i, x in enumerate(b):
    heapq.heappush(q, -x)
    y = heapq.heappop(q)
    s += x + y
    res[-2 - i] -= s

print((max(res)))
