import math


x=list(map(int,input().split()))
y=list(map(int,input().split()))
lt=[]
ln=len(y)
for j in range(ln):
 b=0
 while(b<(ln-j)):
  lt.append(sum(y[b:b+j+1]))
  #print sum(y[b:b+j])
  b+=1
lt.sort()
lt.reverse()
for k in range(x[1]):
 print(lt[k], end=' ')
 
 
   
  

