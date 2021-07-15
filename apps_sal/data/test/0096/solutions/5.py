a, b = input().split()
a = int(a)
b = int(b)

if b == 1:
	print(a)
elif b == 2:
	if a % 2 == 0:
		print(a // 2)
	else:
		print(a-1)
else:

	chopped_even = bin(b+1)[3:]
	len_even = len(chopped_even)
	best_even = ((a - int(chopped_even, 2))//(2**len_even))*2

	chopped_odd = bin(b)[2:]
	len_odd = len(chopped_odd)
	best_odd = ((a - b) // (2**len_odd))*2 + 1

	if best_even > best_odd:
		print(best_even)
	else:
		print(best_odd)
