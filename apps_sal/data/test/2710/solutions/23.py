import sys

cap = [[0 for i in range(300)] for j in range(300)]
flow = [[0 for i in range(300)] for j in range(300)]
inf = 99999999
vis = [0] * 300
par = [0] * 300

def pushflow(v, mf, s):
    if (v == s):
        return mf
    
    u = par[v]
    if (cap[u][v] <= 0):
        mf = min(mf, flow[v][u])
    else:
        mf = min(mf, cap[u][v] - flow[u][v])
    
    mf = pushflow(u, mf, s)
    if (cap[u][v] <= 0):
        flow[v][u] -= mf
    else:
        flow[u][v] += mf
        
    return mf
    
def bfs(n, m, s, t, adj):
    maxflow = 0
    while (1):
        for i in range(2*n):
            vis[i] = 0
        vis[t] = 0
        q = []
        q.append(s)
        vis[s] = 1
        par[s] = -1
        pushed = False
        
        while (len(q) != 0):
            cur = q.pop()
            for i in range(len(adj[cur])):
                nex = adj[cur][i]
                if (vis[nex]):
                    continue
                if (cap[cur][nex] - flow[cur][nex] <= 0 and flow[nex][cur] <= 0):
                    continue
                vis[nex] = 1
                q.append(nex)
                par[nex] = cur
                if nex == t:
                    maxflow += pushflow(t, inf, s)
                    pushed = True
                    break
                
            if pushed:
                break
        if (not pushed):
            break
    return maxflow
    
def main():
    data = [line.rstrip().split() for line in sys.stdin.readlines()]
    data = [[int(x) for x in row] for row in data]
    
    n = data[0][0]
    m = data[0][1]
    
    s = 2*n
    t = 2*n + 1
    adj = [[] for i in range (2*n+10)]
    summing = 0
    for i in range(n):
        u = data[1][i]
        cap[s][i] = u
        summing += u
        adj[s].append(i)
        adj[i].append(s)
    
    check = 0
    for i in range(n):
        u = data[2][i]
        cap[i+n][t] = u
        check += u
        adj[i + n].append(t)
        adj[t].append(i + n)
    if (summing != check):
        print("NO")
        return
    for i in range(n):
        cap[i][i + n] = inf
        adj[i].append(i+n)
        adj[i+n].append(i)
    for i in range(m):
        u = data[i + 3][0]
        v = data[i + 3][1]
        u -= 1
        v -= 1
        cap[u][v + n] = inf
        cap[v][u + n] = inf
        adj[u].append(v + n)
        adj[v + n].append(u)
        adj[v].append(u + n)
        adj[u + n].append(v)
    check = bfs(n, m, s, t, adj)
    if (check == summing):
        print("YES")
        for i in range(n):
            for j in range(n):
                print(flow[i][j + n], end =" ")
            print('\n', end="")
    else:
        print("NO")

main()
        
    
    

