h, w = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(10)]

visited = {}
dist = {}
for i in range(10):
    dist[i] = 100000
dist[1] = 0

while len(dist) > 0:
    cur, curDist = sorted(dist.items(), key=lambda x: x[1])[0]
    del dist[cur]
    visited[cur] = curDist

    for i in range(10):
        if i == cur or i in visited:
            continue

        newDist = curDist + c[i][cur]
        dist[i] = min(dist[i], newDist)

cnts = [0] * 10
for _ in range(h):
    a = list(map(int, input().split()))
    for ai in a:
        if ai != -1:
            cnts[ai] += 1

cnt = 0
for i in range(10):
    cnt += cnts[i] * visited[i]

print(cnt)
