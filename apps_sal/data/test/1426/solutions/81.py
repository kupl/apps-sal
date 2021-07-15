from collections import defaultdict
n,m=list(map(int,input().split()))
d = defaultdict(list)
for _ in range(m):
    u,v=list(map(int,input().split()))
    d[u-1].append(v-1)
S,T=list(map(int,input().split()))
s=S-1
t=T-1
cd=[[0]*3 for _ in range(n)]
cd[s][0]=1
ans=-1
q=[]
q.append([s,0])
while q:
    v,c=q.pop(0)
    if v==t and c%3==0:
        ans=c//3
        break
    for i in d[v]:
        if cd[i][(c+1)%3]==0:
            q.append([i,c+1])
            cd[i][(c+1)%3]=1
print(ans)

