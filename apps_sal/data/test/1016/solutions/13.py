def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if rank[a] < rank[b]:
        p[a] = b
    else:
        p[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1


n, m = list(map(int, input().split()))
rank = [0 for i in range(n)]
p = []
for i in range(n):
    p.append(i)

ans = 1
for i in range(m):
    a, b = list(map(int, input().split()))
    if find(a - 1) != find(b - 1):
        union(a - 1, b - 1)
        ans *= 2
print(ans)
