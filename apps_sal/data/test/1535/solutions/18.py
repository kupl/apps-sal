n, x0, y0 = map(int, input().split())
k = [[None]*2 for i in range(n)]
for i in range(n):
    k[i][0], k[i][1] = map(int, input().split())
    
s = 0
used = [0]*n

for i in range(n):
    f = 0
    x = k[i][0]
    y = k[i][1]
    koef1 = y0-y
    koef2 = x-x0
    koef3 = x0*y-x*y0
    
    if not used[i]:
        f = 1
        used[i] = 1
        
    for j in range(n):
        if not used[j]:
            if koef1*k[j][0] + koef2*k[j][1] + koef3 == 0:
                used[j] = 1
                
    s += f
                
print(s)
