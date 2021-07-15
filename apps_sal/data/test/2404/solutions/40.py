a = int(input())
x = 2
while x**2 <= a:
	while a%x == 0:
		print(x, end = "")
		a //= x
	x += 1
if a > 1: print(a, end = "")
print()

