for i in range(int(input())):
    l,r,d=map(int,input().split())
    if d<l:
        print(d)
    else:
        k=(r+d-1)//d
        ans=k*d
        if ans==r:
            ans+=d
        print(ans)        
