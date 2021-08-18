n, m = list(map(int, input().split()))
to = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    to[u - 1].append(v - 1)

s, t = list(map(int, input().split()))
s -= 1
t -= 1

cnt = 0
phase = 0
q = [s]
visited = [[False] * 3 for _ in range(n)]
while q:
    nextq = []
    for v in q:
        if visited[v][phase]:
            continue
        visited[v][phase] = True
        if v == t and phase == 0:
            print(cnt)
            return
        nextq += to[v]
    if phase == 0:
        cnt += 1
    phase = (phase + 1) % 3
    q = nextq
print((-1))
