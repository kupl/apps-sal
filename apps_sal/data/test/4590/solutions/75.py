#172 緑
from itertools import accumulate
N,M,K=map(int,input().split())
Alist=list(map(int,input().split()))
Blist=list(map(int,input().split()))
cumsum=list(accumulate(Alist))
ans=0
num=0
flag=0
flag1=0
for i in range(N):
    if cumsum[i]>K:
        suma=cumsum[i-1]
        break
else:
    flag1=True
    ans+=1
    num+=1
    suma=cumsum[i]
ans+=i #index注意
num+=i
k=0
while suma+Blist[k]<=K:
    suma+=Blist[k]
    k+=1
    num+=1
    if k==M:
        print(num)
        return
ans=max(ans,num)
for j in range(i+1):
    if flag1:
        suma-=Alist[i-j]
    else:
        suma-=Alist[i-1-j]
    num-=1
    while suma+Blist[k]<=K:
        suma+=Blist[k]
        k+=1
        num+=1
        ans=max(ans,num)
        if k>=M:
            flag=True
            break
    if flag:
        break
ans=max(ans,num)
print(ans)
