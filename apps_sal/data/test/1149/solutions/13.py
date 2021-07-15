n = int(input())
Arr = list(range(1,n+1))
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

X = X[1:]
Y = Y[1:]
for x in X:
	Arr.remove(x)
for y in Y:
	if(y in Arr):
		Arr.remove(y) 
if not Arr:
	print('I become the guy.')
else:
	print('Oh, my keyboard!')
