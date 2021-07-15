import math
x=int(input())
i=2
a=[101]
while True:
    if x==101:
        print(1)
        break
    t=math.floor(a[i-2]+a[i-2]//100)
    a.append(t)
    if t>=x:
        print(i)
        break
    i+=1
