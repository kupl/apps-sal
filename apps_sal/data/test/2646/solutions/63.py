from collections import deque

N, M = [int(x) for x in input().split()]

conn = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = [int(x) for x in input().split()]
    conn[A].append(B)
    conn[B].append(A)

q = deque([1])
signpost = [0] * (N + 1)

while q:
    v = q.popleft()
    for w in conn[v]:
        if signpost[w] == 0:
            signpost[w] = v
            q.append(w)

print('Yes')
for i in range(2, N + 1):
    print(signpost[i])
