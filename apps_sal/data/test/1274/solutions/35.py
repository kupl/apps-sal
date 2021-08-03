from heapq import heapify, heappop, heappush
_, m = map(int, input().split())
work = sorted([tuple(map(int, input().split()))for k in range(_)], key=lambda x: (-x[0], x[1]))
now = []
# print(work)
ans = 0
for i in range(1, m + 1):
    while work and work[-1][0] <= i:
        a, b = work.pop()
        heappush(now, -b)
        # print(a,b)

    if now:
        ans -= heappop(now)
    # print(i,ans)
print(ans)
