import heapq
n = int(input())
l = list(map(int, input().split()))
q = []
for i in range(n):
    heapq.heappush(q, l[i])
a1 = [0] * (n + 1)
a1[0] = sum(l[:n])
for i in range(n):
    p = heapq.heappop(q)
    a1[i + 1] = a1[i] - p + max(p, l[i + n])
    heapq.heappush(q, max(p, l[i + n]))
# print(a1)
q = []
l.reverse()
for i in range(n):
    heapq.heappush(q, -l[i])
a1.reverse()
a1[0] -= sum(l[:n])
z = sum(l[:n])
for i in range(n):
    p = heapq.heappop(q)
    z = z + p + min(-p, l[i + n])
    a1[i + 1] -= z
    heapq.heappush(q, max(p, -l[i + n]))
print((max(a1)))
