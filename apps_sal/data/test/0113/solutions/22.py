def rec(i):
    nonlocal a
    return i
import sys
from collections import Counter
sys.setrecursionlimit(10**6)
#n=int(input())
a,b=list(map(int,input().split()))
z=a
c=0
while a%5==0:
    c=c+1
    a=a//5
d=0
while a%2==0:
    d=d+1
    a=a//2
#c=min(b,c)
#d=min(b,d)
for i in range(b-c):
    z=z*5
for i in range(b-d):
    z=z*2
print(z)

