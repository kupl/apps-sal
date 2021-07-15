import numpy as np
from collections import Counter
N=int(input())
Alist=list(map(int,input().split()))
Q=int(input())
bc=[]
for _ in range(Q):
    bc.append(list(map(int,input().split())))
count=Counter(Alist)
result=0
for key,value in count.items():
    result+=key*value
for i in range(Q):
    if bc[i][0] in count.keys():
        result+=(bc[i][1]-bc[i][0])*count[bc[i][0]]
        count[bc[i][1]]+=count[bc[i][0]]
        count[bc[i][0]]=0
    print(result)
