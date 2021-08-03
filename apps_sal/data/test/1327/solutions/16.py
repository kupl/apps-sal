import heapq
n, m = map(int, input().split())
pml = [[] for _ in range(8)]
for ll in pml:
    heapq.heapify(ll)
for _ in range(n):
    x, y, z = map(int, input().split())
    for xs in [1, -1]:
        for ys in [1, -1]:
            for zs in [1, -1]:
                tempid = (4 if xs == 1 else 0) + (2 if ys == 1 else 0) + (1 if zs == 1 else 0)
                tempspm = x * xs + y * ys + z * zs
                heapq.heappush(pml[tempid], tempspm)
apml = [0] * 8
for i in range(m):
    for xs in [1, -1]:
        for ys in [1, -1]:
            for zs in [1, -1]:
                tempid = (4 if xs == 1 else 0) + (2 if ys == 1 else 0) + (1 if zs == 1 else 0)
                apml[tempid] += - heapq.heappop(pml[tempid])
print(max(apml))
