from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
X = sorted([list(map(int, input().split())) for n in range(N)], key=lambda x: x[0])
hq = []
ans, j = 0, 0

for i in range(1, M + 1):
    while (j < N) and (X[j][0] <= i):
        heappush(hq, -X[j][1])
        j += 1
    if len(hq):
        ans += - heappop(hq)
print(ans)
