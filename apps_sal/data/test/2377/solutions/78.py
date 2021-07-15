import sys
import math
input=sys.stdin.readline

n,h=list(map(int,input().split()))

once=[]
infinity=[]

for i in range(n):
  a,b=list(map(int,input().split()))
  once.append(b)
  infinity.append(a)
  
once.sort(reverse=True)

pin=max(infinity)

once2=[]
for i in range(n):
  if once[i]>pin:
    once2.append(once[i])
  
  else:
      break

ans=0
for i in once2:
    ans+=1
    h-=i
    if h<=0:
        print(ans)
        return

ans+=math.ceil(h/pin)


print(ans)

