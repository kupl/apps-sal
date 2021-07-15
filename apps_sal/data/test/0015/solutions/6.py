a, b, c= [int(i) for i in input().split()]
if (a < b and c<=0) or (a > b and c>=0):
	print("NO")
else:
	if a == b:
		print("YES")
	else:
		if c == 0:
			print("NO")
		else:
			if (b-a)%c == 0:
				print("YES")
			else:
				print("NO")

