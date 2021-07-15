from itertools import accumulate
n=int(input())
d={0:-1}
a=0
for i,b in enumerate(accumulate([2*int(c)-1 for c in input()])):
    x=d.get(b,i)
    d[b]=x
    a=max(a,i-x)
print(a)

