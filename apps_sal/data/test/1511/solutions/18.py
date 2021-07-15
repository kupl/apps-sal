n, m, k = map(int,input().split())
ips = list()
for i in range(n):
    ips.append(list(map(int,input().split())))


locked = [-1] * (n)
lc = [-1] * (k)
for j in range(m):
    cells = [-1] * (k)
    for i in range(n):
        if locked[i] == -1:
            if ips[i][j]-1 > -1:
                if lc[ips[i][j]-1] == -1:
                   if cells[ips[i][j]-1] == -1:
                       cells[ips[i][j]-1] = i
                     
                   else:
                       lc[ips[i][j]-1] = 1
                       locked[i] = j
                       locked[cells[ips[i][j]-1]] = j
                      
                else:
                    locked[i] = j
                    
for i in range(n):
    print(locked[i]+1)
