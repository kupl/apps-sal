import heapq as pq

h = []

n, k, q = list(map(int, input().split()))

ts = list(map(int, input().split()))

for _ in range(q):
    t, i = list(map(int, input().split()))
    if t == 1:
        pq.heappush(h, (ts[i - 1], i))
        if len(h) > k:
            pq.heappop(h)
    else:
        if i in [p[1] for p in h]:
            print('YES')
        else:
            print('NO')
