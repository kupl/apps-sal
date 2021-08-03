
n, q = [int(x) for x in input().split()]
L = [int(x) - 1 for x in input().split()]

G = []
for i in range(n):
    G.append([])
for i in range(n - 1):
    G[L[i]].append((i + 1, L[i]))
    G[i + 1].append((L[i], i + 1))

L = [-1] + L
G[0].reverse()

for t in range(1, n):
    G[t] = [G[t][0]] + list(reversed(G[t][1:]))

options = [(0, 0)]
visited = [0] * n
sub = [1] * n
path = []
while options:
    t = options.pop()
    if visited[t[0]] == 0:
        visited[t[0]] = 1
        path.append(t[0])
        options.extend(G[t[0]])
    elif visited[t[0]] == 1:
        sub[t[0]] += sub[t[1]]

Position = {}
for i in range(n):
    Position[path[i]] = i


for i in range(q):
    u, k = [int(x) for x in input().split()]
    if sub[u - 1] < k:
        print(-1)
    else:
        print(path[Position[u - 1] + k - 1] + 1)
