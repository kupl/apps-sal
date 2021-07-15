from math import *
from collections import *
from bisect import *
import sys
input=sys.stdin.readline
t=int(input())
while(t):
    t-=1
    n=int(input())
    fac=set()
    for i in range(2,int(pow(n,0.5))+1):
        if(n%i==0):
            fac.add(i)
            fac.add(n//i)
    fac.add(1)
    #fac.add(n)
    lcm=float('inf')
    a,b=0,0
    for i in fac:
        if(((i*(n-i))//gcd(i,n-i))<lcm):
            lcm=(i*(n-i))//gcd(i,n-i)
            a,b=i,n-i
    print(a,b)
    
        
            
    
    
    
        
            

