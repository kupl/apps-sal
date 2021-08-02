from collections import deque

n = int(input())
adj = [[] for i in range(n)]
for i in range(n - 1):
    u, v = input().split()
    u, v = int(u), int(v)
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

queue = deque()
queue.append((0, 0))

h = [0 for i in range(n)]
h_even = 1
h_odd = 0

while len(queue) > 0:
    tmp = queue.pop()
    p = tmp[1]
    u = tmp[0]
    for v in adj[u]:
        if v == p:
            continue
        h[v] = h[u] + 1
        if h[v] % 2 == 0:
            h_even += 1
        else:
            h_odd += 1
        queue.append((v, u))

print(h_even * h_odd - n + 1)
