from collections import defaultdict
import sys
input = sys.stdin.readline


class graph:
    def __init__(self, n, mark):
        self.d = defaultdict(list)
        self.n = n
        self.mark = mark

    def add(self, s, d):
        self.d[s].append(d)
        self.d[d].append(s)

    def bfs(self, s, dis):
        marked = s
        visited = [False] * self.n
        visited[s] = True
        q = [s]
        while q:
            s = q.pop(0)
            if(s in mark):
                marked = s
            for i in self.d[s]:
                if(visited[i] == False):
                    q.append(i)
                    visited[i] = True
                    dis[i] += dis[s] + 1
        return marked


n, m, k = list(map(int, input().split()))
mrk = [int(x) for x in input().split()]
mark = {}
for i in mrk:
    mark[i - 1] = 1

g = graph(n, mark)

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    g.add(a - 1, b - 1)
dis = [0] * n
u = g.bfs(0, dis)
dis = [0] * n
d = g.bfs(u, dis)
# print(dis)
temp = [0] * n
x = g.bfs(d, temp)
# print(temp)
count = 0
for i in range(n):
    if(temp[i] <= k and dis[i] <= k):
        count += 1
print(count)
