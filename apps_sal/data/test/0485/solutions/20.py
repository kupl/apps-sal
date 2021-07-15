# https://codeforces.com/contest/1184/problem/C1
n = int(input())
p = []
dx = {}
dy = {}
min_x = None 
max_x = None
min_y = None
max_y = None

for _ in range(4*n+1):
    x, y = list(map(int, input().split()))
    p.append([x, y])
    
    if x not in dx:
        dx[x] = 0
    dx[x] += 1
        
    if y not in dy:
        dy[y] = 0
    dy[y] += 1
    
for x in sorted(dx.keys()):
    if dx[x] >= n:
        min_x = x
        break
        
for x in sorted(dx.keys())[::-1]:
    if dx[x] >= n:
        max_x = x
        break
        
for y in sorted(dy.keys()):
    if dy[y] >= n:
        min_y = y
        break
        
for y in sorted(dy.keys())[::-1]:
    if dy[y] >= n:
        max_y = y
        break    

outlier = None  
#print(min_x, max_x), (min_y, max_y)   

for x, y in p: 
    if (x-min_x)*(x-max_x) <= 0 and (y-min_y)*(y-max_y) <= 0:
        if (x-min_x)*(x-max_x) < 0 and (y-min_y)*(y-max_y) < 0:
            outlier = x, y
            break
    else:
        outlier = x, y
        break
        
print(' '.join([str(x) for x in outlier]))        
#2
#0 0
#0 1
#0 2
#1 0
#1 1
#1 2
#2 0
#2 1
#2 2

