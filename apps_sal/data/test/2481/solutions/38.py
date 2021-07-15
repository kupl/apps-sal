from collections import defaultdict

h,w=map(int,input().split())
c=[]
dic=defaultdict(int)
for _ in range(10): c.append(list(map(int,input().split())))
for _ in range(h):
    temp=list(map(int,input().split()))
    for i in temp: dic[i]+=1
for k in range(10):
    for i in range(10):
        for j in range(10): c[i][j]=min(c[i][j],c[i][k]+c[k][j])
ans=0
for item in dic.items():
    if item[0]>=0: ans+=item[1]*c[item[0]][1]
print(ans)
