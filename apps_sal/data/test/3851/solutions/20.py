import math 
n,k=map(int,input().split())
a,b=map(int,input().split())
w=a-b
w1=a+b
ma=0
m=99999999999999999
for i in range(n):
    l=i*k+w
    tot=(n*k)//(math.gcd(n*k,l))
    ma=max(ma,tot)
    m=min(m,tot)
    l=i*k-w
    tot=(n*k)//(math.gcd(n*k,l))
    ma=max(ma,tot)
    m=min(m,tot)
    l=i*k+w1
    tot=(n*k)//(math.gcd(n*k,l))
    ma=max(ma,tot)
    m=min(m,tot)
    l=i*k-w1
    tot=(n*k)//(math.gcd(n*k,l))
    ma=max(ma,tot)
    m=min(m,tot)
print(m,ma)
