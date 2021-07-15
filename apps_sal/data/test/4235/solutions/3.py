#5671891
from collections import defaultdict as DD
from bisect import bisect_left as BL
from bisect import bisect_right as BR
from itertools import combinations as IC
from itertools import permutations as IP
from random import randint as RI
import sys
MOD=pow(10,9)+7

def IN(f=0):
    if f==0:
        return ( [int(i) for i in sys.stdin.readline().split()] )
    else:
        return ( int(sys.stdin.readline()) )

    
def bfs(s):
    i=1
    parent[s]=-1
    vis[s]=1
    frontier=[s]
    while frontier:
        nex=[]
        for u in frontier:
            for v in d[u]:
                if vis[v]==0:
                    vis[v]=1
                    color[v]=color[u]^1
                    parent[v]=u
                    nex.append(v)
        frontier=nex
        i+=1
    return(parent)

n,m=IN()
d=DD(list)
d1=[]
for i in range(m):
    u,v=IN()
    d[u].append(v)
    d[v].append(u)
    d1.append([u,v])

vis=[0 for i in range(n+1)]

color=[0 for i in range(n+1)]

parent=dict()
for i in range(1,n+1):
    if vis[i]==0:
        bfs(i)
#print(color)

flag=0
for i in d:
    for j in d[i]:
        if color[j]!=color[i]^1:
            flag=1
            break
    if flag==1:
        break


#print("fjfj")
if flag==1:
    print("NO")
else:
    ans=""
    for i,j in d1:
        if color[i]==0 and color[j]==1:
            ans+=str(1)
        else:
            ans+=str(0)
        
    print("YES")
    print(ans)
    

