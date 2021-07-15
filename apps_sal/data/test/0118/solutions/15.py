t, s, x = [int(i) for i in input().split()]
if x < t+s:
	if x == t:
		print("YES")
	else:
		print("NO")
else:	
	if (x-t)%s == 0 or (x-t)%s == 1:
		print("YES")
	else:
		print("NO")

