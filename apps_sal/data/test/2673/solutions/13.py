from collections import defaultdict as dd
s = input().strip()
n = len(s)
vis = [False for i in range(n)]
d = [False for i in range(n)]
V = dd(list)
for i in range(1, n):
    val = ord(s[i]) - 48
    V[val].append(i)
d[0] = 0
vis[0] = True
Q = []
Q.append(0)
while len(Q):
    idx = Q[0]
    if idx == n - 1:
        break
    Q.pop(0)
    val = ord(s[idx]) - 48
    vsz = len(V[val])
    for j in range(vsz):
        nidx = V[val][j]
        if not vis[nidx]:
            vis[nidx] = True
            Q.append(nidx)
            d[nidx] = d[idx] + 1
    V[val].clear()
    if idx - 1 >= 0 and (not vis[idx - 1]):
        vis[idx - 1] = True
        Q.append(idx - 1)
        d[idx - 1] = d[idx] + 1
    if idx + 1 < n and (not vis[idx + 1]):
        vis[idx + 1] = True
        Q.append(idx + 1)
        d[idx + 1] = d[idx] + 1
print(d[n - 1])
