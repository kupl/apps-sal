from math import fabs
a=[int(i)for i in input().split()]
if(a[0]==a[2])|(a[1]==a[3]):print(1,end=' ')
else:print(2,end=' ')
b,c=fabs(a[2]-a[0]),fabs(a[3]-a[1])
if b%2!=c%2:print(0,end=' ')
elif b==c:print(1,end=' ')
else:print(2,end=' ')
print(int(max(fabs(a[2]-a[0]),fabs(a[3]-a[1]))))
