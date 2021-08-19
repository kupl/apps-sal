from heapq import *
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]
heapify(a)
bc = sorted(bc, key=lambda x: x[1], reverse=True)
for (b, c) in bc:
    for i in range(b):
        tmp = heappop(a)
        if tmp >= c:
            heappush(a, tmp)
            break
        else:
            heappush(a, c)
print(sum(a))
