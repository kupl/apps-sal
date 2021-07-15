n=int(input())
a=list(map(int,list(input())))
c8=a.count(8)
t=n//11
if(t>=c8):
	print(c8)
else:
	print(t)
