from heapq import *
n, k = list(map(int, input().split()))
d = list(map(int, input().split()))

res = 0
num = min(k, n)
for i in range(num + 1):
    for j in range(num + 1 - i):
        l = min(k - (i + j), i + j)
        s = d[:i] + d[-j:] if j != 0 else d[:i]
        heapify(s)
        for _ in range(l):
            tmp = heappop(s)
            if tmp > 0:
                heappush(s, tmp)
        res = max(res, sum(s))
print(res)

