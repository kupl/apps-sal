n = input()
a = list(map(int, input().split()))
for i in a:
	if i % 7 == 0 or (i // 7) % 2 == 1 or i <= 14:
		print('NO')
	else:
		print('YES')
