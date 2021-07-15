from collections import deque
n, q = list(map(int, input().split()))
graphs = [set() for _ in range(n)]
for _ in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    graphs[a].add(b)
    graphs[b].add(a)

nodes = [0 for _ in range(n)]
for _ in range(q):
    p, x = list(map(int, input().split()))
    nodes[p - 1] += x

done = [True for _ in range(n)]
D = deque()
D.append([0, 0])
ans = [0 for _ in range(n)]
while D:
    node, value = D.popleft()
    value += nodes[node]
    ans[node] = value
    done[node] = False
    for g in graphs[node]:
        if done[g]:
            D.append([g, value])

print((*ans))

