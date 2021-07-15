#!/usr/bin/env python3

import collections
import sys
input=sys.stdin.readline

n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
cnt1=collections.Counter(arr1)
cnt2=collections.Counter(arr2)
tmp=[[key,cnt1[key]] for key in cnt1.keys()]
tmp=sorted(tmp,reverse=True,key=lambda x:x[1])
arr3=[]
for key,cnt in tmp:
    for _ in range(cnt):
        arr3.append(key)
cnt1=collections.Counter(arr3)
ans=[0]*n
acum=0
pos=0
blank=0
ok=0
head=[]
for key in cnt1.keys():
    tcnt1=cnt1[key]
    tcnt2=cnt2[key]
    acum+=tcnt1
    tpos=max(acum,pos)
    tmp=n-min(tpos,n)
    if blank+tmp<tcnt2:
        print('No')
        return
    blank=min(tpos,n)-ok
    remain=tcnt2
    #print(key,blank,remain)
    for i in range(tpos,n):
        if remain==0:
            break
        ans[i]=key
        ok+=1
        remain-=1
        cnt2[key]-=1
    for _ in range(remain):
        head.append(key)
        cnt2[key]-=1
    pos=min(tpos+tcnt2,n)
    #print(ans,head,pos)
for key in cnt2.keys():
    if cnt2[key]==0:
        continue
    for _ in range(cnt2[key]):
        head.append(key)
pos=0
for i in range(n):
    if ans[i]==0:
        ans[i]=head[pos]
        pos+=1
tmp=[[ans[i],arr3[i]] for i in range(n)]
tmp=sorted(tmp,key=lambda x:x[1])
ans=[tmp[i][0] for i in range(n)]
print('Yes')
print(*ans)
