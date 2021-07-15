from math import *
n,d=map(int,input().split())
c=0
for i in range(n):
    p,q=map(int,input().split())
    if d>=(p**2+q**2)**0.5:
        c+=1
    
print(c)
