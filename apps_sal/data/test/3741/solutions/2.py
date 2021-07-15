import sys
n=int(input())
a=[]

for x in input().split():
    if(int(x)!=int(0)):
        a.append(int(x))

if(len(a)>500):
    print(3)
    return

n=len(a)

#print(n)

g=[]
for i in range(n):
   g.append([])

for i in range(n):
    for j in range(n):
        g[i].append(1000000000)

for i in range(n):
    for j in range(n):
        if(i!=j and (a[i]&a[j])!=0):
            g[i][j]=1


ans=int(10000000000)

dis=[]
for i in range(n):
    dis.append([])

for i in range(n):
    for j in range(n):
        dis[i].append(g[i][j])

for  k in range(n):
    for i in range(k):
        for j in range(i+1,k):
            ans=min(ans,dis[i][j]+g[i][k]+g[k][j])
    for i in range(n):
        for j in range(n):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])



if(ans>1000):
    print(-1)
else:
    print(ans)

