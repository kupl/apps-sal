import sys

n, m = map(int, sys.stdin.readline().split())

hostility = [[] for _ in range(m)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    hostility[i].append(a - 1)
    hostility[i].append(b - 1)

hostility = sorted(hostility, key = lambda x: x[1])

cnt = 0
bridge = -1
for i in range(m):
    if hostility[i][0] <= bridge < hostility[i][1]:
        continue
    bridge = hostility[i][1] - 1
    cnt += 1
print(cnt)
