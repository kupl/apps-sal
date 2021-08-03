import sys
input = sys.stdin.readline

n, m, s = list(map(int, input().split()))
s -= 1
adj = [[] for _ in range(n)]
rev = [[] for _ in range(n)]

for u, v in (list(map(int, input().split())) for _ in range(m)):
    adj[u - 1].append(v - 1)
    rev[v - 1].append(u - 1)

group = [-1] * n
group[s] = 0
stack = [s]

while stack:
    v = stack.pop()
    for dest in adj[v]:
        if group[dest] != -1:
            continue
        group[dest] = 0
        stack.append(dest)

g = 0
for i in range(n):
    if group[i] != -1 or rev[i]:
        continue
    g += 1
    group[i] = g
    stack = [i]

    while stack:
        v = stack.pop()
        for dest in adj[v]:
            if group[dest] != -1:
                continue
            group[dest] = g
            stack.append(dest)

for i in range(n):
    if group[i] != -1:
        continue
    g += 1
    group[i] = g
    stack = [i]

    while stack:
        v = stack.pop()
        for dest in adj[v]:
            if group[dest] == 0 or group[dest] == g:
                continue
            group[dest] = g
            stack.append(dest)

print(len(set(group)) - 1)
