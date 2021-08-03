from collections import deque
N, M = map(int, input().split())

h = [[] * N for _ in range(N)]
AB = []

for _ in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    h[a].append(b)
    h[b].append(a)
    AB.append([a, b])

ans = 0

for i in range(M):
    a, b = AB[i]
    h[a].remove(b)
    h[b].remove(a)

    fl = [False] * N

    q = deque([0])
    while q:
        t = q.popleft()
        if fl[t]:
            continue
        fl[t] = True
        for tt in h[t]:
            q.append(tt)

    if not all(fl):
        ans += 1

    h[a].append(b)
    h[b].append(a)

print(ans)
