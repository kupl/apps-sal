import math;
import time;
import bisect;
def getIntList():
    return list(map(int, input().split()));
def getTransIntList(n):
    first=getIntList();
    m=len(first);
    result=[[0]*n for _ in range(m)];
    for i in range(m):
        result[i][0]=first[i];
    for j in range(1, n):
        curr=getIntList();
        for i in range(m):
            result[i][j]=curr[i];
    return result;
n=int(input());
w=getIntList();
s=input();
p=[int(s[i]) for i in range(2*n)];
seatInt=[(w[i], i) for i in range(n)];
seatInt.sort();
currI=0;
seatExt=[];
result=[0]*(2*n);
for i in range(2*n):
    if p[i]==0:
        result[i]=seatInt[currI][1]+1
        bisect.insort(seatExt, seatInt[currI]);
        currI+=1;
    else:
        result[i]=seatExt.pop()[1]+1;
print(' '.join(map(str,result)))
