import math
a=[int(input()) for i in range(5)]

b=[]
c=[]

for i in range(5):
  p=math.ceil(a[i]/10)*10
  b.append(p)
  c.append(list(str(a[i]-1)))

d=[]
for i in range(5):
  d.append(int(c[i][-1]))

print(sum(b)-(10-min(d)-1))  
