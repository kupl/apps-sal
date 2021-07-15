import heapq as hq
import numpy as np

N, M = map(int, input().split())
job = [list(map(int, input().split())) for _ in range(N)]
ans = 0
job.sort()
job.append([np.inf, np.inf])
jobhq = []
index = 0
for day in range(1, M + 1):
    while day >= job[index][0]:
        hq.heappush(jobhq, - job[index][1])
        index += 1
    if jobhq:
        ans += - hq.heappop(jobhq)
print(ans)
