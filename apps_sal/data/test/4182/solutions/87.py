N,M,X,Y=list(map(int,input().split()))

x=list(map(int,input().split()))
y=list(map(int,input().split()))

if max(X,max(x)) < min(Y,min(y)):
	print("No War")
else:
	print("War")

