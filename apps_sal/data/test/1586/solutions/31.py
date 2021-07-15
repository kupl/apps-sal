N=int(input())
if N%2:
    print(0)
else:
    ans=0
    tmp=10
    while tmp<=N:
        ans+=N//tmp
        tmp*=5
    print(ans)
