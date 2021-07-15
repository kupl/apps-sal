n = int(input())
a = input()
x, y = 0, 0
for i in range(n):
	if a[i] == 'U':
		y += 1
	elif a[i] == 'D':
		y -= 1
	elif a[i] == 'L':
		x -= 1
	elif a[i] == 'R':
		x += 1
print(n - (abs(x) + abs(y)))

