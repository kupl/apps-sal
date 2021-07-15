n,m,k=list(map(int,input().split()))
a,b=list(map(int,input().split()))
p=[]
for i in range(1,n+1):
    p.append(i*m*k)
it=[[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        it[i][j]=j*m*k+k*(i+1)
fl1=True
fl2=True
for i in range(n):
    for j in range(m):
        if it[j][i]-a>=0 and fl1:
            p1=i+1
            it1=j+1
            fl1=False
        if it[j][i]-b>=0 and fl2:
            p2=i+1
            it2=j+1
            fl2=False
        if not fl1 and not fl2:
            break
if p1!=p2:
    t1=min(it1-1+10,5*(it1-1))
    if p1>p2:
        s1=p1
        t21=0
        while s1!=p2:
            s1+=1
            t21+=1
            if s1>n:
                s1//=n
    else:
        s1=p2
        t21=0
        while s1!=p1:
            s1+=1
            t21+=1
            if s1>n:
                s1//=n
    t21*=15
    t2=min(t21,(abs(p2-p1))*15)
    t3=min(it2-1+10,5*(it2-1))
    t=t1+t2+t3
    print(t)
else:
    t=min(abs(it2-it1)*5,10+abs(it2-it1))
    print(t)


