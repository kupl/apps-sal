x, y, z = map(int, input().split())
b = x - y
if abs(b) > z:
	print('-' if b < 0 else '+')
elif z == 0:
	print(0)
else:
	print('?')
