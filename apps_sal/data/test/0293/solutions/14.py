n,i,t,r=int(input()),0,0,[]
while 1:
	i+=1
	n-=i*i
	if n<0:break
	t+=i
	m=n//t 
	r+=[(m+i,i),(i,m+i)][m==0:]*(m*t==n)
print(len(r))
for p in sorted(r):print("%d %d"%p)
