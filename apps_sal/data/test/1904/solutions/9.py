n=int(input())
d=[0]*4
k=input()
g=list(map(int,input().split()))
for i in range(n):
    if('h'==k[i]):
        d[0]+=g[i]
    if('a'==k[i]):
        d[1]=min(d[0],d[1]+g[i])
    if('r'==k[i]):
        d[2]=min(d[1],d[2]+g[i])
    if('d'==k[i]):
        d[3]=min(d[2],d[3]+g[i])
print(min(d))

