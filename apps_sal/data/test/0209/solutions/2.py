x,y=map(int,input().split())
n=int(input())
z=y-x
if n%6==1:
	print(x%1000000007)
elif n%6==2:
	print(y%1000000007)
elif n%6==3:
	print(z%1000000007)
elif n%6==4:
	print((-x)%1000000007)
elif n%6==5:
	print((-y)%1000000007)
else:
	print((-z)%1000000007)
