x, y = map(int, input().split())
 
l = (x*y) % 2
if l == 0:
	print('Even')
else:
 	print('Odd')
