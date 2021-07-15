mod=1000000007
n,k=map(int, input().split())
lst=list(map(int, input().split()))
lst=sorted(lst)
p=1
if lst[-1]==0 and k%2!=0:
    print(0)
elif lst[-1]<0 and k%2!=0:
    for i in range(n-1,n-k-1,-1):
        #print(p)
        p=(p%mod*lst[i]%mod)%mod
    #print(p)
    print(p%mod)
else:
    j=n-1
    if k%2!=0:
        p*=lst[j]
        k-=1
        j-=1
    k=k//2
    i=0
    for x in range(k):
        if lst[i]*lst[i+1]>lst[j]*lst[j-1]:
            p=(p%mod*lst[i]%mod*lst[i+1]%mod)%mod
            i+=2
        else:
            p=(p%mod*lst[j]%mod*lst[j-1]%mod)%mod
            j-=2
    #print(p)
    print(p%mod)
