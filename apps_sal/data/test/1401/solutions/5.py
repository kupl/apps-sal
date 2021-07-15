from sys import *
setrecursionlimit(1000001)
n=int(input())
a=[0]+list(map(int,input().split()))
E=[[] for _ in range(n+1)]
k=[1]*(n+1)
for i in range(n-1):
    p,c=map(int,input().split())
    E[i+2]+=[(p,c)]
    E[p]+=[(i+2,c)]
def bfs(nom,pre=0):
    ch,ii=[(nom,pre)],0
    while ii<len(ch):
        nom,pre=ch[ii]
        for x,c in E[nom]:
            if x!=pre: ch+=[(x,nom)]
        ii+=1
    for i in range(len(ch)-1,-1,-1):
        nom,pre=ch[i]
        for x,c in E[nom]:
            if x!=pre: k[nom]+=k[x]        
    
bfs(1)
def bfs2(nom,pre=0,l=0):
    ch=[(nom,pre,l)]
    ans=0
    while ch!=[]:
        nom,pre,l=ch.pop()
        if l>a[nom]: ans+=k[nom]; continue
        for x,c in E[nom]:
            if x!=pre:  
                ch+=[(x,nom,max(l+c,c))]
    return ans
print(bfs2(1))
