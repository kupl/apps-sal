import heapq
(n, k) = [int(i) for i in input().split()]
power = [int(i) for i in input().split()]
money = [int(i) for i in input().split()]
r = []
for i in range(n):
    r.append((power[i], money[i], i))
r.sort()
cur = 0
ans = [None for i in range(n)]
for i in range(k + 1):
    cur += r[i][1]
    ans[i] = cur
pq = []
for i in range(k + 1):
    pq.append(r[i][1])
heapq.heapify(pq)
for i in range(k + 1, n):
    a = heapq.heappop(pq)
    ans[i] = ans[i - 1] - a + r[i][1]
    heapq.heappush(pq, r[i][1])
end = [None for i in range(n)]
for i in range(n):
    end[r[i][2]] = ans[i]
for i in range(n):
    end[i] = str(end[i])
print(' '.join(end))
