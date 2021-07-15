from itertools import accumulate
n=int(input())
m={0:-1}
a=0
for i,b in enumerate(accumulate([2*int(c)-1 for c in input()])):
    x=m.get(b)
    if x is None:
        m[b]=i
    else:
        a=max(a,i-x)
print(a)

