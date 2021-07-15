import math
import itertools
import sys

n=int(input())
last=input()
log=[]
log.append(last)
q=[]
ans="Yes"
for i in range(n-1):
    tmp=input()
    q.append(tmp)
for i in q:
    if(i[0]!=last[-1] or i in log):
        ans="No"
        break
    else:
        last=i
        log.append(i)
print(ans)

