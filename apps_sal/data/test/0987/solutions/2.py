import sys
input = sys.stdin.readline


def make_set(v):
    parent[v] = v


def find_set(v):
    if v == parent[v]:
        return v
    else:
        parent[v] = find_set(parent[v])
        return parent[v]


def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


n, m = list(map(int, input().split()))

arr = list(map(int, input().split()))

parent = [i for i in range(n)]
rank = [0] * (n)


for i in range(m):
    a, b = list(map(int, input().split()))
    a = a - 1
    b = b - 1
    union_sets(a, b)

b = {}
for i in range(n):
    if find_set(i) not in b.keys():
        b[find_set(i)] = []
    b[find_set(i)].append(i)

e = [0] * n
for i in b:
    b[i].sort()
    c = []
    for j in range(len(b[i])):
        c.append(arr[b[i][j]])
    c.sort(reverse=True)
    for j in range(len(b[i])):
        e[b[i][j]] = c[j]
print(*e)
