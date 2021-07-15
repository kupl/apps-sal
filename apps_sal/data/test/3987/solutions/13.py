import sys
import math
from collections import defaultdict
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
pre=[0]
cnt1,cnt2=0,0
last1,last2=0,0
for i in range(n):
    if arr[i]==1:
        cnt1+=1
        #pre.append(cnt1)
        x=max(last1+1,0)
        pre.append(x)
        last1=x
    else:
        #cnt2+=1
        x=max(last1+1,last2+1)
        pre.append(x)
        last2=x
suf=[0 for _ in range(n+1)]
#cnt1,cnt2=0,0
last1,last2=0,0
for i in range(n-1,-1,-1):
    if arr[i]==1:
        #cnt1+=1
        x=max(last1+1,last2+1)
        suf[i]=x
        last1=x
    else:
        #cnt2+=1
        x=last2+1
        suf[i]=x
        last2=x
ans=max(max(pre),max(suf))
#print(pre,'pre')
#print(suf,'suf')
#print(ans,'ans')
for i in range(1,n+1):
    cnt1,cnt2=0,0
    last1,last2=0,0
    for j in range(i,n+1):
        if arr[j-1]==1:
            x=max(last1+1,last2+1)
            last1=x
            ans=max(pre[i-1]+x+suf[j],ans)
        else:
            x=last2+1
            last2=x
            ans=max(pre[i-1]+x+suf[j],ans)
print(ans)

