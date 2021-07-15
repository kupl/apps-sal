for _ in range(int(input())):
    h,n=map(int,input().split())
    p=list(map(int,input().split()))
    xyz=set(p)
    ans=0
    for i in p:
        if i<h:
            h=i+1
        if(h<=2):
            break
        if i==(h-1):
            if (h-2) in xyz:
                h-=2
            else:
                ans+=1
                h-=2
    print(ans)
