import math

def solve(a,c,d):
    x=a+1
    x-=a//c+1
    x-=a//d+1
    x+=a//(c*d//math.gcd(c,d))+1
    return x

A,B,C,D=list(map(int,input().split()))
print((solve(B,C,D)-solve(A-1,C,D)))

