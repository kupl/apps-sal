import heapq
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.1415926535897932
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l

n,k=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
cnt=[i for i in l if i<0]
m=0
for a,i in enumerate(l):
    if i<0 and m==0:
        m=1
    elif i<0 and l[a-1]>=0:
        m+=1
d={}
q=[]
chk=-1
for i in l:
    if i<0:
        if chk>0:
            if chk in d:
                d[chk]+=1
            else:
                d[chk]=1
                heapq.heappush(q,chk)
        chk=0
    elif chk>=0:
        chk+=1
ans=m*2
k-=len(cnt)
while len(q) and k>=q[0]:
    k-=q[0]
    ans-=2
    d[q[0]]-=1
    if d[q[0]]==0:
        heapq.heappop(q)
if k>=chk and chk>-1:
    ans-=1
print(ans if ans>=0 and k>=0 else -1)
