def split(integer):
	ret = []
	while integer != 0:
		ret.append(integer % 10) # last one
		integer //= 10
	return ret[::-1]

def combine(lst):
	total = 0
	n = len(lst)
	for i in range(n):
		total += 10 ** (n-i-1) * lst[i]
	return int(total)


# al = sorted(list(split(a)))[::-1]
# bl = list(split(b))



# Answer can't have leading zeros.
# Then len(a) == len(b)
# 499200 vs 982400 = b
# 942=a, 911=b
# 9442=a, 9411=b

def solve3(a, b):
	al = sorted(list(split(a)))[::-1]
	bl = list(split(b))
	if len(bl) > len(al):
		print(combine(al))
		return


	if a == b:
		print(a)
		return

	ptr = 0
	n = len(al)
	while ptr < n:
		# print(al, bl, ptr)
		val = bl[ptr]
		selection = al[ptr] # Sorted from high to low
		if selection > val: # illegal:
			k = al.pop(ptr) # pop this idx
			al.append(k)
		if selection == val:
			if ptr == n-1:
				print(combine(al)) # Done to the last one.
				break
			else:
				if combine(sorted(al[ptr+1:])) > combine(bl[ptr+1:]):
					# illegal, min of a_rest is larger than b_rest
					k = al.pop(ptr)
					al.append(k)
				else:
					ptr += 1
					al = al[:ptr] + sorted(al[ptr:])[::-1]
					# print("repermute", al, bl)
					# print(selection)
		if selection < val: # all ptr to the back is legal
			# print("enter")
			# print(al, bl,ptr)

			print(combine(al[:ptr+1] + list(sorted(al[ptr+1:])[::-1])))
			break

a = int(input())
b = int(input())
# solve3(31434123, 13241234)
solve3(a,b)
# solve3(123, 301)
# solve3(4940,5000)
# solve3(942, 911)
# solve3(9442, 9411)
# solve3(3921,10000)
# solve3(9991020, 100001)

