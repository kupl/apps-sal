n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
p=max(a)
t=0
if k>600:
    print(p)
else:
    while t!=k:
        if a[0]>a[1]:
            if a[0]==p:
                print(p)
                return
            m=a[1]
            del a[1]
            a.append(m)
            t+=1
        else:
            m=a[0]
            del a[0]
            a.append(m)
            t=1
    print(a[0])
    

