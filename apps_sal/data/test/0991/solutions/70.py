import heapq
N, M, S = list(map(int, input().split(" ")))
adj = [[] for _ in range(N)]
convert = []
for _ in range(M):
    u, v, a, b = list(map(int, input().split(" ")))
    adj[u - 1].append((v - 1, a, b))
    adj[v - 1].append((u - 1, a, b))

for _ in range(N):
    c, d = list(map(int, input().split(" ")))
    convert.append((c, d))


limit = 2500
S = min(S, limit)
h = [(0, 0, S)]
ans = [[float('inf')] * (limit + 1) for _ in range(N)]

while h != []:
    time_consumed, city, coin = heapq.heappop(h)
    if ans[city][coin] < time_consumed:
        continue
    ans[city][coin] = time_consumed

    if coin + convert[city][0] < limit and ans[city][coin + convert[city][0]] > time_consumed + convert[city][1]:
        ans[city][coin + convert[city][0]] = time_consumed + convert[city][1]
        heapq.heappush(h, (time_consumed + convert[city][1], city, coin + convert[city][0]))

    for v, a, b in adj[city]:
        if coin - a < 0 or ans[v][coin - a] <= time_consumed + b:
            continue
        ans[v][coin - a] = time_consumed + b
        heapq.heappush(h, (time_consumed + b, v, coin - a))

for i in range(1, N):
    print((min(ans[i])))
