x, y, z = list(map(int, input().split()))
x -= y
if x > 0 and z < x:
	print("+")
elif z == 0 and x == 0:
	print("0")
elif x < 0 and abs(z) < abs(x):
	print("-")
else:
	print("?")

