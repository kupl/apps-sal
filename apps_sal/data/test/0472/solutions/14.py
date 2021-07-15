from math import *

def s(x):
    S = 0
    while x!=0:
        S += x%10
        x//=10
    return(S)

def Solve(n):
    sqrt = n**0.5//1
    x = int((10**(log(sqrt,10)//1)))-1

    if((sqrt - x)*log(sqrt,10) >= 10**4):
        x = int(sqrt-10**4)
    
    while(x <= sqrt):
        if x**2+int(s(x))*x == n:
            return(x)
        x+=1
    return(-1)


def solve(n):
    if(n >= 1024974):
        return(Solve(n))
    if(n == 0):
        return(0)
    sqrt = n**0.5//1
    x = int((10**(log(sqrt,10)//1-1)))
    while(x <= sqrt):
        if x**2+int(s(x))*x == n:
            return(x)
        x+=1
    return(-1)



n = int(input())
print(int(solve(n)))

