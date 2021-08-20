(n, m) = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
for nd in g:
    print(len(nd))
