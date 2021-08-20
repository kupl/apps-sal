from heapq import heappush, heappop
from collections import deque
(N, K) = map(int, input().split())
(*B,) = map(int, input())
INF = 10 ** 18
que = deque()
hq = []
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(N):
    a = dp[i]
    while hq and hq[0][1] < i:
        heappop(hq)
    if hq:
        a = min(hq[0][0], a)
    while que and a <= que[-1][1]:
        que.pop()
    que.append((i, a))
    if B[i]:
        heappush(hq, (que[0][1] + (i + 1), i + K + 1))
    if que and que[0][0] <= i - K:
        que.popleft()
    dp[i + 1] = a + (i + 1)
while hq and hq[0][1] < N:
    heappop(hq)
a = dp[N]
if hq:
    a = min(hq[0][0], a)
print(a)
