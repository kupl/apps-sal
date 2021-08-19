import sys
from collections import deque
(N, M) = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    (a, b) = map(int, sys.stdin.readline().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
ars = [0] * N
todo = deque([0])
done = {0}
while todo:
    p = todo.popleft()
    for np in G[p]:
        if np in done:
            continue
        todo.append(np)
        ars[np] = p + 1
        done.add(np)
if len(done) == N:
    print('Yes')
    for i in range(1, N):
        print(ars[i])
else:
    print('No')
