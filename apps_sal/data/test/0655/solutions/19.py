n=int(input())
x,y=map(int,input().split())
w=x+y-2
b=2*n-x-y
if w<=b:
	print("White")
else:
	print("Black")
