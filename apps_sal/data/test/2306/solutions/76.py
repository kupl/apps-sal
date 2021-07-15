f=lambda line,x:line[0]*x+line[1]
def _add_line(line,k,l,r):
    m=(l+r)//2
    if not data[k]:
        data[k]=line
        return
    lx,mx,rx=X[l],X[m],X[r-1]
    left,mid,right=f(line,lx)<f(data[k],lx),f(line,mx)<f(data[k],mx),f(line,rx)<f(data[k],rx)
    if left and right:
        data[k]=line
        return
    if not left and not right:return
    if mid:data[k],line=line,data[k]
    if left!=mid:_add_line(line,2*k+1,l,m)
    else:_add_line(line,2*k+2,m,r)
def add_line(line,a,b):
    L,R=a+N0,b+N0
    a0,b0=a,b
    sz=1
    while L<R:
        if R&1:
            R-=1
            b0-=sz
            _add_line(line,R-1,b0,b0+sz)
        if L&1:
            _add_line(line,L-1,a0,a0+sz)
            L+=1
            a0+=sz
        L>>=1
        R>>=1
        sz<<=1
def query(k):
    x=X[k]
    k+=N0-1
    s=10**18
    while k>=0:
        if data[k]:
            t=f(data[k],x)
            if t<s:s=t
        k=(k-1)//2
    return s
n,*t=map(int,open(0).read().split())
t,v=t[:n],t[n:]
st=sum(t)*2
m=a=i=0
N0=2**(st).bit_length()
data=[None]*(2*N0+1)
X=list(range(st+1))+[10**18]*N0
i=b=0
add_line((.5,0),0,st+1)
for u,w in zip(t,v):
    u+=u+i
    add_line((0,w),i,u)
    add_line((-.5,w+i/2),0,i+1)
    add_line((.5,w-u/2),u,st+1)
    i,b=u,w
add_line((-.5,st/2),0,st+1)
a=x=0
for i in range(1,st+1):
    y=query(i)
    a+=(x+y)/4
    x=y
print(a)
