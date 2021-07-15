import sys
input=sys.stdin.readline

def find_parent(x):
    y=parent[x]
    if y<0:
        return x
    parent[x]=find_parent(y)
    return parent[x]

def connect(a,b):
    c=find_parent(a)
    d=find_parent(b)
    if c==d:
        return
    if parent[c]<parent[d]:
        parent[c]+=parent[d]
        parent[d]=c
    else:
        parent[d]+=parent[c]
        parent[c]=d
    return

def f(S,G):
    que=[S]
    flag=[0]*(N+1)
    L=[0]*(N+1)
    flag[S]=1
    while que:
        H=[]
        for u in que:
            for v,l in data[u]:
                if flag[v]==0:
                    flag[v]=u
                    L[v]=l
                    H.append(v)
                if v==G:
                    break
            else:
                continue
            break
        else:
            que=H
            continue
        break
    qqq=0
    que=G
    while que!=S:
        qqq=max(qqq,L[que])
        que=flag[que]
    return qqq

N,M=map(int,input().split())
X=int(input())

inf=float("inf")
mod=10**9+7

edge=[]
for i in range(M):
    U,V,W=map(int,input().split())
    edge.append([W,U,V])
edge.sort()
parent=[-1]*(N+1)

remain_edge=[]
data=[[] for i in range(N+1)]
weigh=0

for l,a,b in edge:
    if find_parent(a)==find_parent(b):
        remain_edge.append([l,a,b])
        continue
    else:
        connect(a,b)
        weigh+=l
        data[a].append([b,l])
        data[b].append([a,l])
        
if weigh>X:
    print(0)
    return
elif weigh==X:
    count=N-1
    for l,a,b in remain_edge:
        if l==f(a,b):
            count+=1
    print(pow(2,M-count,mod)*(pow(2,count,mod)-2)%mod)
else:
    count_1=0
    count_2=0
    count_3=0
    for l,a,b in remain_edge:
        if weigh-f(a,b)+l==X:
            count_1+=1
        elif weigh-f(a,b)+l<X:
            count_2+=1
        else:
            count_3+=1
    print(2*pow(2,count_3,mod)*(pow(2,count_1,mod)-1)%mod)
