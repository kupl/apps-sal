from collections import defaultdict, deque
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
(q, k) = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(q)]
stack = [-1] * (n + 1)
stack[k] = 0
ed = defaultdict(list)
wt = defaultdict(int)
for e in edges:
    ed[e[0]].append(e[1])
    ed[e[1]].append(e[0])
    wt[e[0], e[1]] = e[2]
    wt[e[1], e[0]] = e[2]
ce = deque([(k, x) for x in ed[k]])
ne = deque()
while True:
    while ce:
        e = ce.pop()
        stack[e[1]] = stack[e[0]] + wt[e]
        for v in ed[e[1]]:
            if stack[v] < 0:
                ne.append((e[1], v))
    if not ne:
        break
    ce.extend(ne)
    ne.clear()
for que in xy:
    print(stack[que[0]] + stack[que[1]])
