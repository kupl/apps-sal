from math import gcd 
p=int(input())-1
cnt=0 
for i in range(1,p):
    if gcd(i,p)==1: cnt+=1 
print(cnt if p!=1 else 1)
