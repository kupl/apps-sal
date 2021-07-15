import sys
sys.setrecursionlimit(10**5)

def find_parent(i):
    aaa=0
    while True:
        if parent[i]<0:
            aaa=i
            break
        else:
            i=parent[i]
    return aaa

def connect(A,B):
    A=find_parent(A)
    B=find_parent(B)
    if A!=B:
        p_A,p_B=parent[A],parent[B]
        if p_A<p_B:
            parent[A]+=p_B
            parent[B]=A
            child[A].append(B)
        else:
            parent[B]+=p_A
            parent[A]=B
            child[B].append(A)

n=int(input())
x_max=0
y_max=0
xy=[]
for _ in range(n):
    x,y=map(int,input().split())
    x_max=max(x_max,x)
    y_max=max(y_max,y)
    xy.append([x,y])
data=[[] for _ in range(x_max+1)]
parent=[-1]*(x_max+1)
child=[[] for i in range(x_max+1)]
lst=[0]*(y_max+1)
for x,y in xy:
    data[x].append(y)
    if lst[y]==0:
        lst[y]=x
    else:
        connect(lst[y],x)

lsls=[]
for i in range(1,x_max+1):
    if parent[i]>=0:
        continue
    if not data[i]:
        continue
    que=[i]
    h=[i]
    while que:
        u=que.pop()
        for v in child[u]:
            que.append(v)
            h.append(v)
    lsls.append(h)

ans=0
for u in lsls:
    L=len(u)
    flag=[0]*(y_max+1)
    cnt=0
    count=0
    for v in u:
        for w in data[v]:
            count+=1
            if flag[w]==0:
                flag[w]=1
                cnt+=1
    ans+=L*cnt-count

print(ans)
