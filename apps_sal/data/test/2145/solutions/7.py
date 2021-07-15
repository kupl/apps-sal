q = int(input())
for re in range(q):
	a, b = map(int,input().split())
	if a >=4:
		print("YES")
	else:
		if a == 1:
			if b == 1:
				print("YES")
			else:
				print("NO")
		if a == 2 or a == 3:
			if b in [1,2,3]:
				print("YES")
			else:
				print("NO")
