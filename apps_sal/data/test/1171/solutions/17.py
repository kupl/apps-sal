from heapq import *
n, k = list(map(int, input().split()))
d = list(map(int, input().split()))

res = 0
num = min(k, n)
for a in range(num + 1):
    for b in range(num + 1 - a):
        trash = k - (a + b)
        s = d[:a] + d[-b:] if b != 0 else d[:a]
        heapify(s)
        for _ in range(min(trash, a + b)):
            tmp = heappop(s)
            if tmp > 0:
                heappush(s, tmp)
                break
        res = max(res, sum(s))
print(res)

