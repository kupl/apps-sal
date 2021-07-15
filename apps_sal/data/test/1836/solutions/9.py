n, m = tuple(map(int, input().split()))

g = [set() for i in range(n + 1)]
for i in range(m):
    a = tuple(map(int, input().split()))
    g[a[1]].add(a[0])
    g[a[0]].add(a[1])
    
res = [0] * (n + 1)
for i in range(1, n+1):
    maxi = 1
    for elem in g[i]:
        if elem > i: continue
        if res[elem] + 1 > maxi: maxi = res[elem] + 1
    res[i] = maxi
    
m = [0] * (n + 1)
for i in range(1, n+1):
    m[i] = res[i] * len(g[i])
    
print(max(m))
        
    

