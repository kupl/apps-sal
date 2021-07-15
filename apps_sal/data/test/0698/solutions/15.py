#! /usr/bin/env python3.3

x, k=list(map(int, input().split()))
a=[False]*x
for i in range(k):
	o=list(map(int, input().split()))
	a[o[1]]=True
	if o[0]==1: a[o[2]]=True
cnt1=cnt2=d=0
for i in range(1,x):
	if a[i]:
		d=0
	else:
		d^=1
		cnt1+=d
		cnt2+=1
print(cnt1, cnt2)


