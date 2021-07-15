import math
from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
d=defaultdict(int)
for i in l:
    d[i]+=1
#print(d)
for i in range(32):
    l1.append(int(math.pow(2,i)))
for i in range(n):
    for j in range(32):
        check=l1[j]-l[i]
        if(check>0):
            if(check==l[i] and d[check]>1):
                c+=1
                break
            elif(check!=l[i] and d[check]>=1):
                c+=1
                break
print(n-c)






