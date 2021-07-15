from math import sqrt as S 
def div(x):
    d=[]
    if x==1:
        return [1]
    if x==2:
        return [1,2]
    cnt=[1,n]
    for i in range(2,int(S(x))+1):
        if x %i==0:
            cnt.append(i) 
    return cnt 
def check(arr):
    if 1 in arr or 0 in arr:
        return 0 
    return len(set(arr))==3 

import sys 
input=sys.stdin.readline 
t=int(input())
ans=[]
for i in range(t): 
    n=int(input()) 
    f=0 
    cnt=div(n)
    for x in cnt : 
        y=n//x
        if f: break 
        for z in div(y):
            if check([x,z,y//z]):
                ans=[x,z,y//z]
                f=1 
                break 
    if f:
        print('YES')
        print(*ans)
    else:
        print('NO')
