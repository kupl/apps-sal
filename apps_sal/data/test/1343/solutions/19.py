import sys
f = sys.stdin

n, m, k = list(map(int, f.readline().strip().split()))

d = dict()
for i in range(m):
    u, v, l = list(map(int, f.readline().strip().split()))
    if d.get(u, -1) == -1:
        d[u] = [[v, l]]
    else:
        d[u].append([v, l])    
        
    if d.get(v, -1) == -1:
        d[v] = [[u, l]]        
    else:
        d[v].append([u, l])
    

if k == 0:
    print(-1)
else:
     
    a = {int(t): 1 for t in f.readline().strip().split()}
        
    s = 2* 10**9    
    city = -1
    
    for it in a:
        if d.get(it, -1) == -1:
            continue
        l_city = d[it]
        for c in l_city:
            if s > c[1] and a.get(c[0], -1) == -1:
                s = c[1]
                city = c[0]
    
    if city == -1:
        print(-1)     
    else:
        print(s)  


