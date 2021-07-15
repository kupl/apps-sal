n,k=map(int,input().split())
a=[i+1 for i in range(n)]
if not k&1:print(-1);return()
k-=1
def f(l,r):
    nonlocal k
    if(k<2 or r-l<2): return
    k-=2
    m=(l+r)//2
    a[m-1],a[m]=a[m],a[m-1]
    f(l,m)
    f(m,r)
f(0,n)
if not k==0:print(-1);return()
for i in a:
    print(int(i),end=" ")


