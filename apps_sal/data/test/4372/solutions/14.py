def gcd(a,b):
    if b==0: return a 
    return gcd(b,a%b)
n=int(input())
l=[int(i) for i in input().split()]
#x total 
#y*z taken 
m=max(l)
d=[m-i for i in l]
g=0 
sm=sum(d)
for i in d:
    g=gcd(i,g)
print(sm//g,g)
