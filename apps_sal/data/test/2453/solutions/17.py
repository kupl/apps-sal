import bisect

n = int(input())
lis = list()
idx = dict()
for i in range(n):
    l,r = map(int,input().split())
    idx[l]=1
    idx[r+1]=1
    lis.append([l,r])
val = [key for key,val in idx.items()]
val.sort()


cnt = [0]*((2*n)+1)
for item in lis:
    f1 = bisect.bisect_left(val,item[0])
    f2 = bisect.bisect_left(val,item[1]+1)
   
    cnt[f1]+=1
    cnt[f2]-=1

for i in range(1,2*n):
    cnt[i]+=cnt[i-1]


ans = [0]*(n+1)

for i in range(1,len(val)):
    sm = val[i]-val[i-1]

    ans[cnt[i-1]]+=sm

for i in range(1,n+1):
    print(ans[i],end=" ")
    
    
