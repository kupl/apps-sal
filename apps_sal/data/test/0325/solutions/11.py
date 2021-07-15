import time

t1 = time.time()

N, M, P = list(map(int, input().split()))
ABC = [tuple(map(int, input().split())) for _ in range(M)]

to_w = [set() for _ in range(N)]
for a, b, c in ABC:
    to_w[a - 1].add((b - 1, P - c))
reachable_from_start = {0}
q = {0}
while q:
    u = q.pop()
    for v, _ in to_w[u]:
        if v not in reachable_from_start:
            reachable_from_start.add(v)
            q.add(v)


from_w = [set() for _ in range(N)]
for a, b, c in ABC:
    from_w[b - 1].add((a - 1, P - c))
reachable_to_goal = {N - 1}
q = {N - 1}
while q:
    u = q.pop()
    for v, _ in from_w[u]:
        if v not in reachable_to_goal:
            reachable_to_goal.add(v)
            q.add(v)


reachable = reachable_from_start & reachable_to_goal


to_w = [set() for _ in range(N)]
for a, b, c in ABC:
    if a - 1 in reachable and b - 1 in reachable:
        to_w[a - 1].add((b - 1, P - c))
d = [float("inf")] * N
d[0] = 0
q = {0}
while q:
    u = q.pop()

    for v, w in to_w[u]:
        tmp = d[u] + w
        if tmp < d[v]:
            d[v] = tmp
            if v not in q:
                q.add(v)

        if time.time() > 1.9 + t1:
            d[-1] = -float("inf")
            break
    else:
        continue
    break

if d[-1] == -float("inf"):
    print((-1))
else:
    print((max(0, -d[-1])))

