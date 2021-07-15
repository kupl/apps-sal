t=int(input())
for magic in range(t):
    n=int(input())
    res=[0 for j in range(n+1)]
    have=[1 for sth in range(n+1)]
    br_p=0
    given=[0]+list(map(int,input().split()))
    for i in range(1,n+1):
        if given[i-1]<given[i]:
            res[i]=given[i]
            have[given[i]]=0
        elif given[i-1]>given[i]:
            br_p=1
            break
    if br_p:
        print(-1)
    else:
        ind_last=1
        for i in range(1,n+1):
            if res[i]==0:
                while have[ind_last]==0:
                    ind_last+=1
                res[i]=ind_last
                ind_last+=1
        for i in range(1,n+1):
            if given[i]<res[i]:
                br_p=1
                break
        if br_p:
            print(-1)
        else:
            print(*res[1:])




