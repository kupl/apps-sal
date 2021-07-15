import sys

n=int(input())
a=input()
a=list(a)
a.reverse()
if n==1:
    print('1')
    return
    
c=1


for i in range(n-1):
    if a[i]!=a[i+1]:
        c+=1

if c==0:
    c+=1
    
print(c)
