def main():
	(n, m) = (int(x) for x in input().split())
	L = [None] * m
	for i in range(m):
		(x, y) = (int(x) for x in input().split())
		L[i] = (x, y)
	print(solver(n, L))

def solver(n, L):
	used = [False] * (n + 1)
	div1 = set()
	div2 = set()
	for (x, y) in L:
		a = max(x, y)
		b = min(x, y)
		if a in div2 or b in div1:
			return 0
		div1.add(a)
		div2.add(b)
		used[a] = True
		used[b] = True
	if len(div1) == 0:
		div1Min = n + 1
	else:
		div1Min = min(div1)
	if len(div2) == 0:
		div2Max = 0
	else:
		div2Max = max(div2)
	if div2Max > div1Min:
		return 0
	else:
		count = 0
		for i in range(div2Max + 1, div1Min):
			if used[i] == False:
				count += 1
		if len(div1) == 0 and len(div2) == 0:
			return count - 1
		elif len(div1) == 0 or len(div2) == 0:
			return count
		else:
			return count + 1
		#if a < div1Min:
		#	div1Min 

main()
# L = [(1, 4), (5, 2)]
# print(solver(5, L))

# L2 = [(1, 2), (2, 3), (1, 3)]
# print(solver(3, L2))

# L3 = [(3, 1), (3, 2)]
# print(solver(3, L3))

#print(solver(2, [(1, 2)]))
# used = [False, True, True, True]
# a = [b for b in used if b == True]
# print(a)
#print(max({1, 2, 3}))

