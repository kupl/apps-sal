'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
import sys
d,k,a,b,t = list(map(int,input().split()))

mn = 10000000000000

if d<=k:
    print(a*d)
    return
    
s = a*k 
d -= k 

if t+s>b*k:
    print(s+b*d)
    return
    
s+=d//k*(t+s)
d%=k

print(s+min(d*b, t+d*a))    
'''
while(d!=0):
    t1 = k*a
    mn = min(mn, t1)
    d-=k'''
    

