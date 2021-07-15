#import resource
#resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
def main():
    mod=998244353
    def ain():
        return list(map(int,sin().split()))
    def sin():
        return sys.stdin.readline().strip()
    """*********************************************************************************"""
    def dfs(x):
        if(p[x]==0):
            p[x]=1
            pt[0]+=1
            for i in de[x]:
                if(t[x]==1):
                    if(t[i]==1):
                        s[0]=0
                        return
                    else:
                        if(p[i]!=1):
                            t[i]=2
                            dfs(i)
                else:
                    if(t[i]==2):
                        s[0]=0
                        return
                    else:
                        if(p[i]!=1):
                            t[i]=1
                            r[0]+=1
                            dfs(i)
    h=[]
    pow1=[1]
    s=1
    for i in range(300000):
        s=(s*2)%mod
        pow1.append(s)
    for _ in range(int(input())):
        n,m=ain()
        de=[[] for i in range(n)]
        for i in range(m):
            x,y=ain()
            de[x-1].append(y-1)
            de[y-1].append(x-1)
        p=[0]*n
        s1=1
        t=[0]*n
        for i in range(n):
            if(p[i]==0):
                s=[1]
                pt=[0]
                t[i]=1
                r=[1]
                dfs(i)
                if(s[0]==1):
                    r1=pt[0]-r[0]
                    r2=r[0]
                    r1=(pow1[r1]+pow1[r2])%mod
                    s1=(s1*r1)%mod
                else:
                    s1=0
                    break
        h.append(str(s1))
    sys.stdout.write("\n".join(h))
threading.Thread(target=main).start()

