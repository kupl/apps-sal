n = int(input())
x = n // 10
y = x * 10
if abs(y - n) > 5:
	print(y + 10)
else:
	print(y)	
