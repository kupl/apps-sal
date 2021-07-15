n,k=list(map(int,input().split()))
#b=[i for i in range(1,n+1)]
r=n%(2*k+1)
a=[]
if n<=2*k+1:
    a.append((n+1)//2)
    print(len(a))
    print(*a)
    return
if r>=k+1 or r==0:
    l=[i for i in range(k+1,n+1,2*k+1)]
    print(len(l))
    print(*l)
else:
    d=k+1-r
    s=k+1-d
    l=[i for i in range(s,n+1,2*k+1)]
    print(len(l))
    print(*l)

