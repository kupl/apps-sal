import heapq
(n, k) = map(int, input().split())
pq = [0] * k
res = [None] * n
for i in range(n):
    (s, m) = map(int, input().split())
    time = max(pq[0], s) + m
    heapq.heapreplace(pq, time)
    res[i] = time
print('\n'.join(map(str, res)))
