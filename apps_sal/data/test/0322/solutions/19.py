import sys
import math
c1=0
c2=0
for xxx in range(int(input())):
    n,m=(list(map(int,sys.stdin.readline().split(' '))))
    if(n<0):
        c1+=1
    if(n>0):
        c2+=1
if(c1<=1 or c2<=1):
    print("Yes")
else:
    print("No")

