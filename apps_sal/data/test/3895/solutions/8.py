n = int(input())
f = [0] + list(map(int, input().split()))
vis = set()
same = set()
for i in range(1, n + 1):
    vis.add(f[i])
    if f[i] == i:
        same.add(f[i])
if len(vis) > len(same):
    print(-1)
    quit()
m = len(same)
same = [0] + list(same)
g = [0 for i in range(n + 1)]
h = [0 for i in range(m + 1)]
for i in range(1, m + 1):
    h[i] = same[i]
    g[same[i]] = i
for i in range(1, n + 1):
    g[i] = g[f[i]]
print(m)
print(*g[1:], sep=' ')
print(*h[1:], sep=' ')
