def dfs(node, g) :
    nonlocal visited, M, N
    for i in range(N) :
        if M[node][i] == '0' or visited[i] : continue
        visited[i] = True
        g.append(i)
        dfs(i, g)
    
N = int(input())
P = list(map(int, input().split(' ')))
M = [input() for i in range(N)]

G = []
visited = [False]*N
for i in range(N) :
    if visited[i] : continue
    visited[i] = True
    g = [i]
    dfs(i, g)
    g.sort()
    G.append(g)

for g in G :
    for i in range(len(g)) :
        for j in range(i+1, len(g)) :
            if P[g[i]] > P[g[j]] : P[g[i]], P[g[j]] = P[g[j]], P[g[i]]

ans = ""
for i in range(len(P)) :
    ans += str(P[i]) + ' '
ans = ans[:-1]
print(ans)
    

