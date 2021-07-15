A, B, X, Y = map(int, input().split())

if A == B:
	print(X)
elif A > B:
	if 2*X < Y:
		print(2*X*(A-B-1)+X)
	else:
		print(Y*(A-B-1)+X)
else:
	if 2*X < Y:
		print(2*X*(B-A)+X)
	else:
		print(Y*(B-A)+X)
