from bisect import bisect_left as lower_bound,bisect_right as upper_bound
for _ in range(int(input())):
    n,k=map(int,input().split())
    x=sorted(map(int,input().split()))
    input()
    mxr=[0]*n
    for i in range(n-1,-1,-1):
        mxr[i]=i-lower_bound(x,x[i]-k)+1
    ans=1
    cmxr=mxr[0]
    for i in range(1,n):
        res=cmxr
        cmxr=max(cmxr,mxr[i])
        cf=upper_bound(x,x[i]+k)-i
        ans=max(ans,res+cf)
    print(ans)

'''
1
7 1
1 5 2 3 1 5 4

'''
