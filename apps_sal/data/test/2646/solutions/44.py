from collections import deque
N, M = map(int, input().split())
C = [[] for i in range(N + 1)]
for i in range(M):
    A, B = sorted(list(map(int, input().split())))
    C[A].append(B)
    C[B].append(A)

d = [-1] * (N + 1)
d[0] = 0
d[1] = 0

queue = deque([1])
while queue:
    now = queue.popleft()
    for i in C[now]:
        if d[i] != -1:
            continue
        d[i] = now
        queue.append(i)

if d.count(0) > 2:
    print('No')
    exit
print('Yes')
for i in range(2, N + 1):
    print(d[i])
