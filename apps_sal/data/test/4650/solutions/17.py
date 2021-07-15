from sys import stdin
q=int(stdin.readline().strip())
for i in range(q):
    n=int(stdin.readline().strip())
    s=list(map(int,stdin.readline().strip().split()))
    u=0
    z=0
    d=0
    for i in range(n):
        s[i]=s[i]%3
        if s[i]==0:
            z+=1
        elif s[i]==1:
            u+=1
        else:
            d+=1
    ans=0
    ans+=z
    ans+=min(u,d)
    if u<=d:
        d-=u
        x=0
        for i in range(d):
            x+=2
            x=x%3
            if x==0:
                ans+=1
    else:
        u-=d
        x=0
        for i in range(u):
            x+=1
            x=x%3
            if x==0:
                ans+=1
    print(ans)
            

