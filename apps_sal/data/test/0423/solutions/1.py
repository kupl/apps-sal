n, k = map(int, input().split())
a = []

check = 0
for _ in range(n + 1):
	new_a = input()
	if new_a == '?':
		check += 1
	else:
		new_a = int(new_a)

	a.append(new_a)

if check > 0:
	if k != 0:
		if (n + 1) % 2 == 0:
			print('Yes')
		else:
			print('No')
	else:
		if ((n + 1 - check) % 2 == 1 and a[0] == '?') or a[0] == 0:
			print('Yes')
		else:
			print('No') 
else:
	module1 = 2**58 - 203
	module2 = 2**64 - 59
	result1 = result2 = result3 = 0
	for c in a[::-1]:
		result1 = (result1 * k + c) % module1
		result2 = (result2 * k + c) % module2
		result3 = (result3 * k + c) % (module1 + module2)

	if result1 == 0 and result2 == 0 and result3 == 0:
		print('Yes')
	else:
		print('No')
