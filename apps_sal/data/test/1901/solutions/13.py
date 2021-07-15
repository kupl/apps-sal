import sys, threading
sys.setrecursionlimit(100010)
threading.stack_size(67108864)

res = 0

def main():
    n,m=list(map(int,input().split()))
    c=[int(c) for c in input().split()]
    g={}
    
    
    flag=[0 for i in range(n) ]
    
     
    for i in range(n):
        g[i]=[]
        
    for i in range(m):
        p,o=list(map(int ,input().split()))
        o-=1
        p-=1
        g[o].append(p)
        g[p].append(o)
        
    def glu(v,p,k):
        nonlocal res
        if flag[v]==0:
            flag[v]=k
            for i in g[v]:
                if i!=p:
                    glu(i,v,k)
    k=1
    for i in range(n):
        l=flag[i]
        glu(i,-1,k)
        if l==0:
            k+=1
    mn={}
    for i in range(max(flag)):
        mn[i]=10**9 
    for i in range(n):
        if mn[flag[i]-1]>=c[i]:
            mn[flag[i]-1]=c[i]
    su=0
    for i in range(len(mn)):
            su+=mn[i]    
    print(su)    
    
    

thread = threading.Thread(target=main)
thread.start()

