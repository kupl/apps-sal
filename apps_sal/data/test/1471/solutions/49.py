N = int(input())
dist_from_1 = [0 for i in range(N+1)]

paths = [dict() for i in range(N+1)]
for i in range(N-1):
    a, b, dist = list(map(int, input().split()))
    paths[a][b] = dist
    paths[b][a] = dist

queue = [(0, 1, 0)]
while len(queue) != 0:
    prev, now, dist = queue.pop()
    dist_from_1[now] = dist
    for next in paths[now]:
        if next == prev:
            continue
        queue.append((now, next, dist + paths[now][next]))

for i in range(1, N+1):
    if dist_from_1[i] % 2 == 0:
        print((0))
    else:
        print((1))

