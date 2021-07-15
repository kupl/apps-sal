n=int(input())
a=list(map(int,input().split()))
def f(x):
    p=1
    re=0
    for i in range(n):
        re+=abs(p-a[i])
        p*=x
    return re
def g():
    re=0
    for i in range(n):
        re+=a[i]-1
    return re
a.sort()
if n>32:
    print(g())
    return
i=1
ans=10**18
while 1:
    tmp=f(i)
    if ans<tmp: break
    ans=tmp
    i+=1
print(ans)

