import heapq

N, M, S = list(map(int, input().strip().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, A, B = list(map(int, input().strip().split()))
    u -= 1
    v -= 1
    graph[u].append((v, A, B))
    graph[v].append((u, A, B))

exchanges = []
for _ in range(N):
    C, D = list(map(int, input().strip().split()))
    exchanges.append((C, D))

queue = [(0, 0, S)]
max_fare = 2500

state_table = [[None] * (max_fare + 1) for i in range(N)]

reached = [False] * N
reached_count = 0

while queue:
    time, cur, money = heapq.heappop(queue)
    if not reached[cur]:
        reached[cur] = True
        reached_count += 1
        if reached_count >= N:
            break
    count, d_time = exchanges[cur]
    for n, A, B in graph[cur]:
        n_money = money - A
        n_time = time + B
        if n_money >= 0:
            states = state_table[n]
            if n_money > max_fare:
                n_money = max_fare
            if states[n_money] == None or states[n_money] > n_time:
                states[n_money] = n_time
                heapq.heappush(queue, (n_time, n, n_money))

    states = state_table[cur]
    money += count
    time += d_time
    if money >= 0:
        if money > max_fare:
            money = max_fare
        if states[money] == None or states[money] > time:
            states[money] = time
            heapq.heappush(queue, (time, cur, money))


for i in range(1, N):
    states = state_table[i]
    minimum = None
    for t in states:
        if t != None and (minimum == None or minimum > t):
            minimum = t
    print(minimum)
