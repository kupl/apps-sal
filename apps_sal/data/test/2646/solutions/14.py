from collections import deque

N, M = list(map(int, input().split()))

route = [[] for i in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    route[a - 1].append(b - 1)
    route[b - 1].append(a - 1)

print('Yes')

q = deque()
d = [-1] * N
d[0] = 0
q.append(0)

while q:
    x = q.popleft()
    for i in route[x]:
        if d[i] == -1:
            d[i] = x + 1
            q.append(i)

for i in range(1, N):
    print((d[i]))
