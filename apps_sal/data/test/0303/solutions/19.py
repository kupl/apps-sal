x1, y1, x2, y2 = map(int, input().split())
x, y = map(int, input().split())

deltaX = abs(x2-x1)
deltaY = abs(y2-y1)

# if (deltaY // y) == (deltaX // x):
# 	print("YES")
# elif (deltaY // x) == (deltaX // y):
# 	print("YES")
# elif (deltaX % x == 0) and (deltaY == 0):
# 	print("YES")
# elif (deltaY % y == 0) and (deltaX == 0):
# 	print("YES")
# elif deltaX == deltaY == 0:
# 	print("YES")
# else:
# 	print("NO")

if ((y2-y1)%(2*y) == 0) and ((x2-x1)%(2*x) == 0):
	print("YES")
elif ((x2-x-x1)%(2*x) == 0) and ((y2-y-y1)%(2*y) == 0):
	print("YES")
else:
	print("NO")
