from collections import deque
K = int(input())
E = [[(i * 10) % K, (i + 1) % K] for i in range(K)]
INF = K * 10
V = [INF] * (K)
V[1] = 1
q = deque([1])
i = 1
while q:
    i = q.popleft()
    if V[E[i][0]] > V[i]:
        q.appendleft(E[i][0])
        V[E[i][0]] = V[i]
    if V[E[i][1]] > V[i] + 1:
        q.append(E[i][1])
        V[E[i][1]] = V[i] + 1
print(V[0])
