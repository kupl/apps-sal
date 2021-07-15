n = int(input())
a = map(int, input().split(' '))
for elem in a:
	if elem % 2 == 0:
		print(elem - 1, end=' ')
	else:
		print(elem, end=' ')

