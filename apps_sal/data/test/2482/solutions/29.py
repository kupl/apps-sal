from collections import deque

n, k, l = map(int, input().split())
ep = [[] for i in range(n)]
er = [[] for i in range(n)]

gp = [-1] * n
gr = [-1] * n

for i in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ep[a].append(b)
    ep[b].append(a)
for i in range(l):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    er[a].append(b)
    er[b].append(a)


def dfs(e, g):
    count = 0
    for i in range(n):
        if g[i] == -1:
            g[i] = count

            q = deque([])
            q.append(i)
            while q:
                now = q.pop()

                for nex in e[now]:
                    if g[nex] == -1:
                        g[nex] = g[now]
                        q.append(nex)
            count += 1

    return g


gp = dfs(ep, gp)
gr = dfs(er, gr)
l = []
dic = {}
for i in range(n):
    s = (gp[i], gr[i])
    l.append(s)
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
ans = [0] * n

for i in range(n):
    ans[i] = dic[l[i]]
print(*ans)
