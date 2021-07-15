def check(x):
	if x < 3:
		return False
	if x == 3:
		return True
	if x % 7 == 0:
		return True
	if x % 3 == 0:
		return True
	else:
		return check(x - 3)				

n = int(input())
for _ in range(n):
	x = int(input())
	if check(x):
		print("YES")
	else:
		print("NO")	
