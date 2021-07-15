m,k=list(map(int,input().split()))
if 2**m<=k or m*k==1:
    print((-1))
elif m==1 and k==0:
    print("0 0 1 1")
else:
    ans=[-1 for i in range(2**(m+1))]
    sta=2**m-1
    cnt=0
    for i in range(1,2**m):
        if cnt==k:
            cnt+=1
        ans[sta+i]=cnt
        ans[sta-i]=cnt
        cnt+=1
    ans[sta]=k
    ans[-1]=k
    
    print((" ".join([str(i) for i in ans])))
    

