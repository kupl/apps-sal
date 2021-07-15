import sys
input = sys.stdin.readline

n=int(input())
E=[[] for i in range(n+1)]

for i in range(n-1):
    x,y=list(map(int,input().split()))
    E[x].append(y)
    E[y].append(x)

def dfs(t):
    L=[-1]*(n+1)
    L[t]=0

    Q=[t]

    while Q:
        x=Q.pop()
        for to in E[x]:
            if L[to]==-1:
                L[to]=L[x]+1
                Q.append(to)

    return L.index(max(L))

A=dfs(1)
B=dfs(A)

DEPTH=[-1]*(n+1)
DEPTH[1]=0

from collections import deque
QUE = deque([1])
QUE2 = deque()
EULER=[]

USED=[0]*(n+1)
while QUE:
    x=QUE.pop()
    EULER.append((DEPTH[x],x))
    if USED[x]==1:
        continue
    for to in E[x]:
        
        if USED[to]==0:
            DEPTH[to]=DEPTH[x]+1
            QUE2.append(to)
        else:
            QUE.append(to)
    QUE.extend(QUE2)
    QUE2=deque()
 
    USED[x]=1

MINP=[1<<30]*(n+1)
MAXP=[-1]*(n+1)

for ind,(depth,p) in enumerate(EULER):
    MINP[p]=min(MINP[p],ind)
    MAXP[p]=max(MAXP[p],ind)

LEN=len(EULER)

seg_el=1<<(LEN.bit_length())
SEG=[(1<<30,0)]*(2*seg_el)

for i in range(LEN):
    SEG[i+seg_el]=EULER[i]

for i in range(seg_el-1,0,-1):
    SEG[i]=min(SEG[i*2],SEG[i*2+1])

def update(n,x,seg_el):
    i=n+seg_el
    SEG[i]=x
    i>>=1
    
    while i!=0:
        SEG[i]=min(SEG[i*2],SEG[i*2+1])
        i>>=1
        
def getvalues(l,r):
    L=l+seg_el
    R=r+seg_el
    ANS=(1<<30,0)

    while L<R:
        if L & 1:
            ANS=min(ANS , SEG[L])
            L+=1

        if R & 1:
            R-=1
            ANS=min(ANS , SEG[R])
        L>>=1
        R>>=1

    return ANS

def LCA(l,r):
    return getvalues(min(MINP[l],MINP[r]),max(MAXP[l],MAXP[r])+1)

A2=DEPTH[A]*2+DEPTH[B]*2-LCA(A,B)[0]*2
ANS=0

for i in range(1,n+1):
    if i==A or i==B:
        continue

    if ANS<A2+DEPTH[i]*2-LCA(i,A)[0]*2-LCA(i,B)[0]*2:
        ANS=A2+DEPTH[i]*2-LCA(i,A)[0]*2-LCA(i,B)[0]*2
        Aind=i

print(ANS//2)
print(A,B,Aind)
    
    

