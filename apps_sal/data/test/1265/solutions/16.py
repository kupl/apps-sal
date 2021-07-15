A = input()
B = input()
if(len(A)!=len(B)):
	print("NO")
else:
	A1 = "1" in A
	B1 = "1" in B
	if(A1 == B1):
		print("YES")
	else:
		print("NO")
