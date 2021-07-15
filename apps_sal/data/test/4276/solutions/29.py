import math
from statistics import mean
# a=int(input())
#b=int(input())
# c=[]
# for i in b:
#     c.append(i)
e1,e2 = list(map(int,input().split()))
#f = list(map(int,input().split()))
#j = [input() for _ in range(3)]
h = []
for i in range(e1):
    h.append(list(map(int,input().split())))
r=[]
count=0
for i in range(e1):
    if h[i][1]<=e2:
         r.append(h[i][0])

if len(r)>0:
    print((min(r)))
else:
    print("TLE")



