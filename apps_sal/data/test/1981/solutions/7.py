from collections import deque


class edge:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def other(self, x):
        if x == self.x:
            return self.y
        else:
            return self.x


n, m = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
adj = [[edge(0, 0) for j in range(1)] for i in range(n)]
for i in range(n - 1):
    xi, yi = list(map(int, input().split(' ')))
    adj[xi - 1].append(edge(xi - 1, yi - 1))
    adj[yi - 1].append(edge(xi - 1, yi - 1))

answer = 0


marked = [False] * n
pi = [-1] * n
count = [0] * n
k = 0
queue = deque()
pi[k] = k
queue.append(k)
marked[k] = True
while len(queue) > 0:
    v = queue[0]
    queue.popleft()
    if a[v] == 1 and a[pi[v]] == 1:
        count[v] = count[pi[v]]
    if a[v] == 1:
        count[v] += 1
    #print("m :",m," count[v] :",count[v])
    if count[v] > m:
        marked[v] = True
        continue
    c = 0
    for e in adj[v]:
        w = e.other(v)
        if not marked[w]:
            queue.append(w)
            pi[w] = v
            marked[w] = True
    #		print(w)
            c += 1
    #print("c :", c," m :",m," pi[",v,"] " ,pi[v], " count[",v,"]:",count[v])
    if c == 0 and count[v] <= m:
        answer += 1

print(answer)
