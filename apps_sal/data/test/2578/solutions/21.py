import sys
sys.setrecursionlimit(1000000)
(nUsers, nGroups) = map(int, sys.stdin.readline().split())
parent = list(range(nUsers + 1))
rank = [0] * (nUsers + 1)


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    (idA, idB) = (find(a), find(b))
    if idA == idB:
        return
    if rank[idA] > rank[idB]:
        parent[idB] = idA
    else:
        parent[idA] = idB
        if rank[idA] == rank[idB]:
            rank[idB] += 1


for _ in range(nGroups):
    g = sys.stdin.readline()
    if g[0] >= '1':
        g = list(map(int, g.split()))
        for i in range(2, len(g)):
            union(g[1], g[i])
count = [0] * (nUsers + 1)
for user in range(nUsers + 1):
    count[find(user)] += 1
ret = []
for user in range(1, nUsers + 1):
    ret.append(str(count[parent[user]]))
sys.stdout.write('%s\n' % ' '.join(ret))
