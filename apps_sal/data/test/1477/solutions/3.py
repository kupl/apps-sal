from sys import stdin
from collections import deque

n, m = [int(x) for x in stdin.readline().split()]

e = [int(x) for x in stdin.readline().split()]
graph = [set() for x in range(n)]
reverse = [set() for x in range(n)]
root = set([x for x in range(n)])

for edge in range(m):
    a, b = [int(x) for x in stdin.readline().split()]
    graph[b].add(a)
    reverse[a].add(b)
    if a in root:
        root.remove(a)

done = set()

qMain = deque(list(root))
qCo = deque()

total = -1

while len(done) < n:
    total += 1
    while qCo:
        nxt = qCo.popleft()
        #print('co', nxt)
        if e[nxt] == 0:
            qMain.append(nxt)
        else:
            done.add(nxt)
            for x in graph[nxt]:
                reverse[x].remove(nxt)
                if not reverse[x]:
                    qCo.append(x)

    while qMain:
        nxt = qMain.popleft()
        #print('main', nxt)
        if e[nxt] == 1:
            qCo.append(nxt)
        else:
            done.add(nxt)
            for x in graph[nxt]:
                reverse[x].remove(nxt)
                if not reverse[x]:
                    qMain.append(x)

print(total)
