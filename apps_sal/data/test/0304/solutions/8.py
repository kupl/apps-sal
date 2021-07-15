n = input()
facts = {0: 1}

def fact(a):
	nonlocal facts
	if a in facts:
		return facts[a]
	res = 1
	for i in range(1, a+1):
		res *= i
		facts[i] = res
	return facts[a]

occ = [0] * 10
for i in range(len(n)):
	occ[int(n[i])] += 1

ans = 0

def go_find(hame, start):
#	print("Start: " + str(start))
#	print(hame)
	nonlocal ans
	if hame[0] == 0:
		res = fact(sum(hame))
		for i in range(10):
			res //= fact(hame[i])
	else:
		res2 = fact(sum(hame)-1)
		for i in range(1, 10):
			res2 //= fact(hame[i])
		res2 //= fact(hame[0]-1)
		
		res = fact(sum(hame))
		for i in range(10):
			res //= fact(hame[i])

		res -= res2

#	print(res)
#	print("=============")
	ans += res
	for i in range(start, 10):
		if hame[i] > 1:
			hame[i] -= 1
			go_find(hame, i)
			hame[i] += 1

go_find(occ, 0)
print(ans)
	


