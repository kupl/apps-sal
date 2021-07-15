n,i,t,r=int(input()),0,0,[]
while n>=0:
	i+=1
	n-=i*i
	t+=i
	m=n//t+i
	r+=[(m,i),(i,m)][m==i:]*(n%t==0<=n)
for p in[(len(r),'')]+sorted(r):print("%d %s"%p)
