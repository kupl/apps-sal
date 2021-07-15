__author__ = 'Utena'
n=int(input())
m=int(input())
x=sorted([int(input())for i in range(n)])
t=0
for j in range(n):
    m-=x[n-j-1]
    t+=1
    if m<=0:
        break
print(t)
