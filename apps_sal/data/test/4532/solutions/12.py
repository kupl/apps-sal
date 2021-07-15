import collections

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(n):
        arr[i]%=k
    cnt=collections.Counter(arr)
    ans=0
    for key in cnt.keys():
        if key==0:
            continue
        tmp=(k-key)%k+k*(cnt[key]-1)
        ans=max(ans,tmp+1)
    print(ans)
