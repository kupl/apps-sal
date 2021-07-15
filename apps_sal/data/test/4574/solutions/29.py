from collections import Counter

N=int(input())
A=list(map(int,input().split()))

c = Counter(A)
mc=[]
for k in c.keys():
  if c[k]>=2:mc.append(k)
    
if len(mc)==0:
  print(0)
  return

elif len(mc)==1:
  if c[mc[0]]<4:
    print(0)
    return
  else:
    print(mc[0]**2)
    return
  
mc = sorted(mc,reverse=True)
if c[mc[0]] < 4:print(mc[0]*mc[1])
else:print(mc[0]**2)
