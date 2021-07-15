instr, days = (int(x) for x in input().split())
# print (instr, days)
arr = [(int(y), x + 1) for x, y in enumerate(input().split())]
arr.sort()
if arr[0][0] > days:
	print(0)
else:
	result = []
	for hard in arr:
		days -= hard[0]
		if days >= 0:
			result.append(str(hard[1]))
		else:
			break
	print(len(result))
	print(" ".join(result))

