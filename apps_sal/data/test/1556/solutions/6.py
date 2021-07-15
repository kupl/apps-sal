import heapq

n, k, x = [int(val) for val in input().split()]
a = [int(val) for val in input().split()]

data = [(val, 1, i) if val >= 0 else (-1 * val, -1, i) for i, val in enumerate(a)]
heapq.heapify(data)
sign = sum([1 if s == -1 else 0 for _, s, _ in data])

if sign % 2 == 1:
    for i in range(k):
        e = heapq.heappop(data)
        heapq.heappush(data, (e[0] + x, e[1], e[2]))
else:
    e = heapq.heappop(data)
    if e[0] <  k * x:
        s = (e[0] // x) + 1
        k -= s
        heapq.heappush(data, (s * x - e[0], -1 * e[1], e[2]))
        for i in range(k):
            e = heapq.heappop(data)
            heapq.heappush(data, (e[0] + x, e[1], e[2]))
    else:
        heapq.heappush(data, (e[0] - k * x, e[1], e[2]))

output = [0] * n
for val, s, i in data:
    output[i] = s * val
print(' '.join([str(val) for val in output]))
   

