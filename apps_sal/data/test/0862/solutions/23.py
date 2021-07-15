import math
n = int(input().strip())
a=[int(x) for x in input().strip().split(' ')]
minm = 1000000000000000000
ans = 0
for i in range(n):
    v=a[i]-i
    if max(0,v)==0:
        if 0<minm:
            ans = i+1
            minm=0
    else:
        b = round(math.ceil(v/n)+1)
        if b<minm:
            ans = i+1
            minm=b
print(ans)
