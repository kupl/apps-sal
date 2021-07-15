import sys
input=sys.stdin.readline
from collections import defaultdict
 
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=defaultdict(int)
for i in range(n):
    c[a[i]]+=1


s=0
for i in range(n):
    for j in c:
        if c[j]>1:
            if j|a[i]==j:
                s+=b[i]
                break
print(s)
