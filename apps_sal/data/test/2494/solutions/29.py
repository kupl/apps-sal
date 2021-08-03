from collections import deque
k = int(input())

e = [[] for i in range(k)]
for i in range(k):
    e[i].append(((i + 1) % k, 1))
    if i * 10 % k != i:
        e[i].append(((i * 10) % k, 0))

d = [-1] * k
d[1] = 0
q = deque([])
q.append((1, 0))
while q:
    now, dis = q.popleft()

    for nex, cost in e[now]:
        if d[nex] == -1 or d[nex] > dis + cost:
            d[nex] = dis + cost
            if cost == 0:
                q.appendleft((nex, dis))
            else:
                q.append((nex, dis + 1))

print(d[0] + 1)
