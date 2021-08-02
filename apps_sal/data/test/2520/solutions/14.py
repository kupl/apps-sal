n, m, k = map(int, input().split())
root = [i for i in range(n)]
height = [1 for i in range(n)]


def find(n):
    sn = n
    while n != root[n]:
        n = root[n]
    root[sn] = n
    return n


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    elif height[a] >= height[b]:
        height[a] += height[b]
        height[b] = 0
        root[b] = a
    else:
        height[b] += height[a]
        height[a] = 0
        root[a] = b


l = [set() for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    union(a, b)
    l[a].add(b)
    l[b].add(a)
for i in range(k):
    a, b = map(lambda x: int(x) - 1, input().split())
    if find(a) == find(b):
        l[a].add(b)
        l[b].add(a)
print(*[height[find(i)] - len(l[i]) - 1 for i in range(n)])
