n, m = list(map(int, input().split()))
adj = [0] * (n + 1)
for i in range(n + 1):
    adj[i] = []
s = 0
for i in range(m):
    x, y = list(map(int, input().split()))
    adj[x].append(y)
    adj[y].append(x)
    if len(adj[x]) > len(adj[s]):
        s = x
    if len(adj[y]) > len(adj[s]):
        s = y
stk = []
mp = {}
mp[s] = 1
for i in range(len(adj[s])):
    stk.append([s, adj[s][i]])
    if adj[s][i] not in mp:
        mp[adj[s][i]] = 1
i = 0
# for l in mp:
# 	print (l)
while(i < len(stk)):
    k = stk[i][1]
    for j in range(len(adj[k])):
        if k not in mp or adj[k][j] not in mp:
            stk.append([k, adj[k][j]])
            mp[k] = 1
            mp[adj[k][j]] = 1
    i += 1
for i in range(len(stk)):
    print(*stk[i])
