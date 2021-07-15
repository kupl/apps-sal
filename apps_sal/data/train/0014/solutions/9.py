for __ in range(int(input())):
	a,b=map(int,input().split())
	x,y=map(int,input().split())
	if(a==x and b+y==x):
		print("Yes")
	elif(a==y and b+x==y):
		print("Yes")
	elif(b==x and a+y==x):
		print("Yes")
	elif(b==y and a+x==y):
		print("Yes")
	else:
		print("No")
