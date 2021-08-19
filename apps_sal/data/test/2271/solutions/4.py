def read():
    return list(map(int, input().split()))


n = int(input())
g = [list() for i in range(n + 1)]
for i in range(n - 1):
    (a, b) = read()
    g[a].append(b)
    g[b].append(a)
cnt = 0
for i in range(n + 1):
    k = len(g[i])
    cnt += k * (k - 1) // 2
print(cnt)
