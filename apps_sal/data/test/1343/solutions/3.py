from sys import stdin, stdout
(n, m, k) = map(int, stdin.readline().split())
vertices = [[] for i in range(n + 1)]
for i in range(m):
    (a, b, w) = map(int, stdin.readline().split())
    vertices[a].append((b, w))
    vertices[b].append((a, w))
if k:
    storages = set(map(int, stdin.readline().split()))
    ans = float('inf')
    for num in storages:
        for v in vertices[num]:
            if v[0] not in storages:
                ans = min(ans, v[1])
    if ans == float('inf'):
        stdout.write('-1')
    else:
        stdout.write(str(ans))
else:
    stdout.write('-1')
