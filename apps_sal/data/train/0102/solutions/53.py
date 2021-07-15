t=int(input())
for i in range(t):
    n=int(input())
    l=len(str(n))
    if n<10:
        ans=n
    else:
        ans=l*9-9
        k=str(n)[0]
        k=int(k*l)
        if k<=n:
            ans+=int(str(n)[0])
        else:
            ans+=int(str(n)[0])-1
    print(ans)

