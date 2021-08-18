from queue import deque

n = int(input())
a = [0] + list(map(int, input().split()))

G = {i: [] for i in range(1, n + 1)}

for i in range(1, n):
    parent, edge = list(map(int, input().split()))
    G[parent].append((i + 1, edge))

cut = 0
stack = [(1, 0, False)]

while stack:
    v, cur_max, to_cut = stack.pop()

    if cur_max > a[v] and not to_cut:
        to_cut = True
        cut += 1

    if to_cut:
        cut += len(G[v])

    for u, e in G[v]:
        stack.append((u, max(0, cur_max + e), to_cut))

print(cut)
