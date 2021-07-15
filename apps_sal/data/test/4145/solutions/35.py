import math

x=int(input())

if x==2:
    print((2))
    return

x=x//2*2+1
i=x
while 1:
    flag=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=False
            break
    if flag:
        break
    i+=1

print(i)

