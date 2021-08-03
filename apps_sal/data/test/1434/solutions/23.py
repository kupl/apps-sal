n = int(input())
ss = [0] * n
degs = [0] * n
leaves = []
for i in range(n):
    degs[i], ss[i] = list(map(int, input().split()))
    if degs[i] == 1:
        leaves.append(i)

edges = []
while len(leaves) != 0:
    leaf = leaves.pop()
    if degs[leaf] == 0:
        continue
    v = ss[leaf]
    edges.append((leaf, v))
    v_deg = degs[v]

    ss[v] = ss[v] ^ leaf
    degs[v] -= 1
    if degs[v] == 1:
        leaves.append(v)

print(len(edges))
for edge in edges:
    print(edge[0], edge[1])
