for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    q=-1
    t=0
    r=[]
    for i in range(n):
        if a[i]<q or a[i]<i+1:
            t=1
            break
        else:
            q=a[i]
    if t==1:
        print(-1)
    else:
        q=-1
        w=[True]*n
        z=0
        for i in range(n):
            if a[i]>q:
                r.append(a[i])
                w[a[i]-1]=False
                q=a[i]
            else:
                while w[z]==False:
                    z+=1
                r.append(z+1)
                z+=1
        print(*r)

