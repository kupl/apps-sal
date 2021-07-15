N=int(input())
csf=[list(map(int,input().split()))for _ in range(N-1)]
i=0
while i<N:
    ans=0
    j=i
    while j<N-1:
        c,s,f=list(csf[j])
        ans=max(ans,s)
        if ans%f:
            ans+=f-ans%f
        ans+=c
        j+=1
    print(ans)
    i+=1
