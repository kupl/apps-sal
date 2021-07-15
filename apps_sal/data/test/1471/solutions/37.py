import sys
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

done = {}
todo = [(0, 0, 0)]
while todo:
    i, c, d = todo.pop()
    for ni, dd in G[i]:
        if ni in done:
            continue
        nd = d + dd
        nc = nd % 2
        todo.append((ni, nc, nd))
    done[i] = c

for i in range(N):
    print(done[i])
