import  sys
#input=sys.stdin.readline
dp={}
mod=int(1000000007)
sys.setrecursionlimit(100000)
def bigmod(n,p):
    p=int(p)
    if p==0:
        return 1
    x=bigmod(n,p/2)
    x=(x*x)%mod
    if p%2==1:
        x=(x*n)%mod
    return x
k,pa,pb=list(map(int,input().split()))
r=bigmod(pa+pb,mod-2)
r1=bigmod(pb,mod-2)
r1=(pa*r1)%mod
p=(pa*r)%mod
q=(pb*r)%mod



def cal(k1,a1):
    if k1+a1>=k:
        return (k1+a1+r1)%mod
    if (k1,a1) in dp:
        return dp[(k1,a1)]
    dp[(k1,a1)]=((cal(k1+a1,a1)*q)%mod+(cal(k1,a1+1)*p)%mod)%mod
    return dp[(k1,a1)]

print(cal(0,1))


