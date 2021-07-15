n,s = [int(item) for item in input().split()]
g = [0 for i in range(n+10)]
for i in range(n-1):
    u,v  = [int(item) for item in input().split()]
    g[u] += 1
    g[v] += 1 
c = 0
for i in range(1, n+1):
    if (g[i] == 1):
        c += 1
print(2*s/c)
