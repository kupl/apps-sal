n,Sum=list(map(int,input().split()))
if n==1 and Sum==0:
    print(0,0)
elif Sum==0 or Sum>9*n:
    print(-1,-1)
else:
    l=[0]*n
    r=[0]*n
    b,p="",""
    s=Sum
    for i in range(n):
        if s>=9:
            r[i]=9
            s-=9
        else:
            r[i]=s
            s=0
        l[n-i-1]=r[i]
    if l[0]!=0:
        for i in range(n):
            b=b+str(l[i])
            p=p+str(r[i])
        print(b,p)
    else:
        for i in range(n):
            if l[i]!=0:
                break
        l[0]='1'
        l[i]=l[i]-1
        for i in range(n):
            b=b+str(l[i])
            p=p+str(r[i])
        print(b,p)

