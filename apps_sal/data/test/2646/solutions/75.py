from collections import defaultdict, deque

N, M = map(int, input().split())
path = defaultdict(list)

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    path[A].append(B)
    path[B].append(A)

prev = [0] * N
dist = [0] * N
q = deque([0])

while (len(q) > 0):
    a = q.popleft()
    for b in path[a]:
        if dist[b] != 0:
            continue
        q.append(b)
        prev[b] = a
        dist[b] = dist[a] + 1

print('Yes')

for a in prev[1:]:
    a += 1
    print(a)
