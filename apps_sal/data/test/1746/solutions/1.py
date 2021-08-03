def read(): return list(map(int, input().split()))


n = int(input())
g = [list() for i in range(n + 1)]
for i in range(n - 1):
    p = int(input())
    g[p].append(i + 2)
c = [0] * (n + 1)
for i in range(1, n + 1):
    if len(g[i]) == 0:
        c[i] = 1
for i in range(1, n + 1):
    if not c[i]:
        cnt = 0
        for u in g[i]:
            cnt += c[u]
        if cnt < 3:
            print('No')
            return
print('Yes')
