x=int(input())
point=x//11+1
point*=2
if x%11<=6:
  point-=1
if x%11==0:
  point-=1
print(point)
