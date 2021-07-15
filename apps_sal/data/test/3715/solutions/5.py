def main():
	n = input()
	L = [int(x) for x in input().split()]
	print(solver(L))

def solver(L):
	return helper(L, None)

def helper(L, last):
	if len(L) == 0:
		return 0
	x = L[0]
	if last == "gym":
		if L[0] in [0, 2]:
			return 1 + helper(L[1:], None)
		elif L[0] in [1, 3]:
			return helper(L[1:], "contest")
	elif last == "contest":
		if L[0] in [0, 1]:
			return 1 + helper(L[1:], None)
		elif L[0] in [2, 3]:
			return helper(L[1:], "gym")
	elif last == None:
		if L[0] == 0:
			return 1 + helper(L[1:], None)
		elif L[0] == 1:
			return helper(L[1:], "contest")
		elif L[0] == 2:
			return helper(L[1:], "gym")
		elif L[0] == 3:
			for i in range(1, len(L)):
				if L[i] == 0:
					return 1 + helper(L[i + 1:], None)
				elif L[i] == 1:
					return helper(L[i + 1:], "contest")
				elif L[i] == 2:
					return helper(L[i + 1:], "gym")
			return 0
	else:
		assert(False)

# print(solver([1, 3, 2, 0]))
# print(solver([1, 3, 3, 2, 1, 2, 3]))
# print(solver([2, 2]))

main()
