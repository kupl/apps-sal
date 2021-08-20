from collections import deque
N = int(input())
E = []
G = {i: set() for i in range(1, N + 1)}
c = [-1 for i in range(N - 1)]
for i in range(N - 1):
    (a, b) = list(map(int, input().split()))
    E.append({a, b})
    G[a].add(i)
    G[b].add(i)
Q = deque([0])
c[0] = 1
while Q:
    i = Q.popleft()
    (a, b) = E[i]
    n = len(G[a])
    color = 0
    count = 0
    for ni in G[a]:
        if c[ni] == -1:
            c[ni] = color + 1
            if c[ni] >= c[i]:
                c[ni] += 1
            color += 1
            Q.append(ni)
        else:
            count += 1
            if count > 1:
                break
    n = len(G[b])
    color = 0
    count = 0
    for ni in G[b]:
        if c[ni] == -1:
            c[ni] = color + 1
            if c[ni] >= c[i]:
                c[ni] += 1
            color += 1
            Q.append(ni)
        else:
            count += 1
            if count > 1:
                break
print(max(c))
for i in c:
    print(i)
