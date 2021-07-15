import math;
import random;
import time;
import heapq;
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
n = int(input());
t= input();
for d in range(1, n+1):
    if n%d==0:
        t1=t[:d];
        t=t1[::-1]+t[d:];
print(t);

