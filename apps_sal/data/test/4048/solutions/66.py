import sys

n=int(input())

c=[]

for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        c.append(i+n//i-2)

if len(c)==0:
    print(n-1)
    return
    
print(min(c))
