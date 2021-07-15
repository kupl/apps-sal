import math as mt
a=[int(input()) for i in range(5)]
for i in range(5):
    if a[i]%10!=0 and a[i]%10<a[0]%10:
        a[0],a[i]=a[i],a[0]
t=[mt.ceil(a[i]/10)*10 for i in range(1,5)]
print(a[0]+sum(t))
