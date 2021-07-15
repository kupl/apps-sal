import collections
from collections import defaultdict
import math


#for _ in range(int(input())):
#n=int(input())
#s=input()
#n,m=[int(x) for x in input().split()]
n,z=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
p=min(a) 
q=max(a)
for i in range(z):
 if p<=int(input())<=q:
   print("Yes")
 else:
  print("No") 
