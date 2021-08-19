from collections import deque
print('Yes')
(N, M) = map(int, input().split())
net = [[] for _ in range(N + 1)]
vect = [0] * (N + 1)
for _ in range(M):
    (A, B) = map(int, input().split())
    net[A].append(B)
    net[B].append(A)
q = deque()
q.append(1)
while len(q) > 0:
    t = q.popleft()
    for i in net[t]:
        if t != i and vect[i] == 0:
            vect[i] = t
            q.append(i)
for i in range(2, N + 1):
    print(vect[i])
