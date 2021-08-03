import heapq

N, M, S = map(int, input().split())

uvab = [list(map(int, input().split())) for _ in range(M)]
cd = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    uvab[i][0] -= 1
    uvab[i][1] -= 1

railways = [[] for _ in range(N)]
max_a = 0
for u, v, a, b in uvab:
    railways[u].append((v, a, b))
    railways[v].append((u, a, b))
    max_a = max(max_a, a)
del uvab

max_silver = max_a * (N - 1)

ans = [-1] * N
d = dict()
d[(S, 0)] = 0  # silver, station
Q = [(0, S, 0)]  # time, silver, station
sum_reached = 0
reached = [False] * N

while Q:
    t, sv, st = heapq.heappop(Q)
    if not reached[st]:
        ans[st] = t
        reached[st] = True
        sum_reached += 1
        if sum_reached == N:
            break

    new_key = (min(max_silver, sv + cd[st][0]), st)
    new_value = t + cd[st][1]
    if new_key not in d or d[new_key] > new_value:
        d[new_key] = t + cd[st][1]
        heapq.heappush(Q, (new_value, *new_key))

    for dist, a, b in railways[st]:
        if sv >= a:
            new_key = (sv - a, dist)
            new_value = t + b
            if new_key not in d or d[new_key] > new_value:
                d[new_key] = new_value
                heapq.heappush(Q, (new_value, *new_key))

print(*ans[1:], sep="\n")
