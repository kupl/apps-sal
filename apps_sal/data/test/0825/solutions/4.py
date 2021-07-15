import math
from collections import defaultdict
from itertools import accumulate
N=int(input())
data=defaultdict(int)
result=0
for i in range(2,int(math.sqrt(N))+1):
    while N%i==0:
        N//=i
        data[i]+=1
if N!=1:
    data[N]+=1
cumsum=list(accumulate(range(1,10**6*2)))
for value in data.values():
    for i in range(10**6*2):
        if value<cumsum[i]:
            result+=i
            break
if result==0:
    if N!=1:
        result=1
print(result)
