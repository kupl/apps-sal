

import numpy as np
a,b,c = list(map(int,input().split()))
L = np.array([a,b,c])
d = (L%2).sum()

def calc(a,b,c):
    e = a+b+c
    max1 = max(a,b,c)
    min1 = min(a,b,c)
    mid = e - max1 - min1
    return (max1*2 - mid - min1)//2
    
if d == 3 or d == 0:
    print((calc(a,b,c)))
elif d == 1:
    if a%2 ==1:
        b +=1
        c +=1
        print((calc(a,b,c)+1))
    elif b%2 == 1:
        a +=1
        c +=1
        print((calc(a,b,c)+1))
    elif c%2 == 1:
        a +=1
        b +=1
        print((calc(a,b,c)+1))
elif d == 2:
    if a%2 == 0:
        b +=1
        c +=1
        print((calc(a,b,c)+1))
    elif b%2 == 0:
        a +=1
        c +=1
        print((calc(a,b,c)+1))
    elif c%2 == 0:
        a +=1
        b +=1
        print((calc(a,b,c)+1))
        


