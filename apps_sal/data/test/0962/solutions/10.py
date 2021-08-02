from heapq import heappop, heappush

n, m = map(int, input().split())
xy = [tuple(int(x) - 1 for x in input().split()) for _ in range(m)]

R = [[] for _ in range(n)]
h = [0] * n

for x, y in xy:
    R[x].append(y)
    h[y] += 1

S = []

st = []

for i in range(n):
    if h[i] == 0:
        heappush(st, i)

while len(st) > 0:
    temp = heappop(st)
    S.append(temp)
    for x in R[temp]:
        h[x] -= 1
        if h[x] == 0:
            heappush(st, x)

if len(S) != n:
    print(-99999)
else:
    print(-1)
