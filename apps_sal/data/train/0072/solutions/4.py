import collections

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    if len(collections.Counter(arr))>k:
        print(-1)
    else:
        cand=list(collections.Counter(arr).keys())
        cnt=len(cand)
        for i in range(1,n+1):
            if cnt>=k:
                break
            else:
                if i not in cand:
                    cand.append(i)
                    cnt+=1
        print(cnt*n)
        print(*(cand*n))
