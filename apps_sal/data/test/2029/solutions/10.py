(n, s) = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
cnt = 0
for i in range(n):
    if len(g[i]) == 1:
        cnt += 1
print(2 * s / cnt)
