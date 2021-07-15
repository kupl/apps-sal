import sys
input = sys.stdin.readline

t=int(input())

import math

def f(x):
    
    xr=math.ceil(math.sqrt(x))

    LIST=[]
    for i in range(1,xr+1):
        if x%i==0:
            LIST.append(i)
            LIST.append(x//i)

    return sorted(set(LIST))[1:]


for test in range(t):
    n=int(input())
    L=f(n)

    A=L[0]

    for i in f(n):
        if i!=A and i*A<n and n%(i*A)==0 and n//(i*A)!=i and n//(i*A)!=A and n//(i*A)!=1:
            print("YES")
            print(A,i,n//(i*A))
            break

    else:
        print("NO")
    
    

