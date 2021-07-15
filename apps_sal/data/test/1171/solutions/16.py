import heapq
N, K = list(map(int, input().split()))
d = [int(x) for x in map(int, input().split())]
e = d[::-1]

res = 0
num = min(N, K)
for i in range(num + 1):
    for j in range(num - i, -1, -1):
        s = d[:i] + e[:j]
        if not s:
            continue
        heapq.heapify(s)
        res = max(res, sum(s))
        l = min(i + j, K - (i + j))
        while l:
            heapq.heappop(s)
            res = max(res, sum(s))
            l -= 1
print(res)

