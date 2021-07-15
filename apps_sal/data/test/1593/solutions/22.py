import math
n,m=map(int, input().split())
L=[]
for i in range(n):
     x,y,z=map(int, input().split())
     L.append( (math.sqrt(x*x+y*y),z) )
L.sort()
count=m
if count>=1000000:
     print('0')
     return
for i in L:
     count+=i[1]
     if count>=1000000:
          print(i[0])
          return
print('-1')
