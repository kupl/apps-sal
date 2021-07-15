from heapq import *
INF = float('inf')
n, m = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
wg= ng = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

aaa = set(map(int, input().split()))
if len(aaa) == 1:print((min(aaa)));print((0));return
rm = []
for i in range(n+1):
    ng[i] = len(adj[i])
    if i not in aaa and ng[i] == 1: rm.append(i)

for a in aaa: ng[a] = 0

def remove_node(index):
    while adj[index]:
        nx = adj[index].pop()
        adj[nx].remove(index)
        ng[nx] -= 1
        if ng[nx] == 1: rm.append(nx)

    ng[index] = 0

while rm: remove_node(rm.pop())

state = [0 for _ in range(n+1)]
que = [(min(aaa), None)]
res = 0
for _ in range(2):
    deep = [0 for _ in range(n + 1)]
    while que:
        res += 1
        root, proot = que.pop()
        for nx in adj[root]:
            if proot == nx:
                continue
            if _: state[nx] = root
            deep[nx] = deep[root] + 1
            que.append((nx, root))
    if _: break

    start = max(1,deep.index(max(deep)))
    que = [(start, None)]

end = max(1, deep.index(max(deep)))
i = end
path = 1
while i != start:
    path += 1
    i = state[i]

print(min(start,end))
print(res -1 -path)

