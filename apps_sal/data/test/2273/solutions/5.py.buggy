"""
NTC here
"""
from sys import setcheckinterval, stdin, setrecursionlimit
setcheckinterval(1000)
setrecursionlimit(10**7)

# print("Case #{}: {} {}".format(i, n + m, n * m))


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


def BFS(s, adj):
    parent = {s: None}
    color = [-1] * (len(adj))
    color[s] += 1
    u = [s]
    while u:  # runs till u is []
        nextu = []
        for i in u:
            for v in adj[i]:
                if v not in parent:
                    color[v] = (color[i] + 1) % 3
                    parent[v] = i
                    nextu.append(v)
                else:
                    if color[v] == color[i]:
                        color[v] = (color[v] + 1) % 3
        u = nextu.copy()
    for i in range(len(adj)):
        color[i] += 1
    return color


n, m = lin()
adj = [[] for i in range(n)]
for _ in range(m):
    i, j = lin()
    adj[i - 1].append(j - 1)
    adj[j - 1].append(i - 1)

sol = BFS(0, adj)
c1 = [0, 0, 0]  # count of 1,2,3
for i in sol:
    if i == 0:
        print(-1)
        return
    c1[i - 1] += 1
ch = [[0 for i in range(3)] for j in range(3)]  # 12,13,23

for v in range(n):
    for u in adj[v]:
        ch[sol[v] - 1][sol[u] - 1] += 1
#        ch[sol[u]-1][sol[v]-1]+=1
        if sol[v] == sol[u]:
            print(-1)
            return
a12 = ch[0][1] + ch[1][0]
a13 = ch[0][2] + ch[2][0]
a23 = ch[1][2] + ch[2][1]
# print(a12,a13,a23,c1,sol)
if a12 == 2 * c1[0] * c1[1] and a13 == 2 * c1[0] * c1[2] and a23 == 2 * c1[1] * c1[2]:
    print(*sol)
else:
    print(-1)
