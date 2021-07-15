# ez
import math
pown = 1
ind = []
f = []
pw = []
 
def get(l,r):
    x = pw[r - l + 1]
    if f[r][x] > f[l+p2[x]-1][x]:
        return f[r][x]
    return f[l + p2[x] - 1][x]

def solve(x,y):
    if y <= x:
        return 0
    p = get(x,y)
    if y - p[1] <= p[1] - x:
        cur = 0
        for i in range(p[1] , y + 1):
            if ind[p[0] - a[i]] >= x and ind[p[0] - a[i]] <= p[1]:
                cur = cur + 1
        return cur + solve(x , p[1] - 1) + solve(p[1] + 1 , y)
    else:
        cur = 0
        for i in range(x , p[1] + 1):
            if ind[p[0] - a[i]] >= p[1] and ind[p[0] - a[i]] <= y:
                cur = cur + 1
        return cur + solve(x , p[1] - 1) + solve(p[1] + 1 , y)

n = int(input())
 
for i in range(0 , 200005):
    pw.append(0)
p2 = []
p2.append(1)
for i in range(1,20):
    p2.append(p2[i - 1] * 2)
for i in range(0,18):
    for j in range(p2[i] , p2[i + 1]):
        if j <= 200000:
            pw[j] = i
 
arr = [int(i) for i in input().split()]
a = []
a.append(0)
for i in range(0 , n):
    a.append(arr[i])
for i in range(0 , n+1):
    ind.append(0)
 
for i in range(1 , n + 1):
    ind[a[i]] = i
for i in range(1 , 200005):
    ad = []
    for j in range(0 , 19):
        ad.append((0 , 0))
    f.append(ad)
 
for i in range(1 , n + 1):
    f[i][0] = (a[i] , i)
    for j in range(1 , 18):
        f[i][j] = f[i][j - 1]
        if i - p2[j] >= 0 and f[i - p2[j - 1]][j - 1] > f[i][j]:
            f[i][j] = f[i - p2[j - 1]][j - 1]
ans = 0

q = []

q.append((1 , n))
maxind = 1
num = 0
while num < maxind:
    x = q[num][0]
    y = q[num][1]
    #print(x , y)
    p = get(x,y)
    #print(p)
    if y - p[1] <= p[1] - x:
        for i in range(p[1] , y + 1):
            #print(i , a[i])
            if ind[p[0] - a[i]] >= x and ind[p[0] - a[i]] <= p[1]:
                ans += 1
    else:
        for i in range(x , p[1] + 1):
            if ind[p[0] - a[i]] >= p[1] and ind[p[0] - a[i]] <= y:
                ans += 1
    if x < p[1] - 1:
        q.append((x , p[1] - 1))
        maxind += 1
    if y > p[1] + 1:
        q.append((p[1] + 1 , y))
        maxind += 1
    num += 1
    #print(num , maxind)

print(ans)

