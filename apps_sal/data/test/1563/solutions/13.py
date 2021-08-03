n, m = map(int, input().split())
a = list(map(int, input().split()))
gr = [set() for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    gr[u - 1].add(v - 1)
    gr[v - 1].add(u - 1)
tr = {}
for i in range(max(a)):
    tr[i] = set()
for i in range(n):
    b = a[i]
    for j in gr[i]:
        if a[j] != b:
            tr[b - 1].add(a[j] - 1)

ans = 0
pos = min(a)
for i in range(max(a)):
    if len(tr[i]) > ans:
        ans = len(tr[i])
        pos = i + 1

print(pos)
