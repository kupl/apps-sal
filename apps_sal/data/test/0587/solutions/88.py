
from heapq import heappop, heappush

INF = 10 ** 18

N, K = map(int, input().split())
S = [[] for _ in range(N)]
for _ in range(N):
    t, d = map(int, input().split())
    S[t - 1].append(d)

for i in range(N):
    S[i].sort(reverse=True)
    if not S[i]:
        S[i].append(-INF)

S.sort(reverse=True)

uma = 0
que = []
for i in range(K):
    uma += S[i][0]
    for j in range(1, len(S[i])):
        heappush(que, (-1) * S[i][j])

for i in range(K, N):
    for j in range(len(S[i])):
        heappush(que, (-1) * S[i][j])

ans = uma + K * K
for x in range(K - 1, 0, -1):
    v = S[x][0]
    w = (-1) * que[0]
    if v < w:
        heappop(que)
        heappush(que, (-1) * v)
        uma -= v
        uma += w
    ans = max(ans, uma + x * x)

print(ans)
