n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = [0]*(len(a)+1)

valids = dict()
for a1 in range(4):
	for b1 in range(4):
		valids[str(a1)+str(b1)] = list()
		for t1 in range(4):
			for t2 in range(4):
				if (t1 | t2 == a1 and t1 & t2 == b1):
					valids[str(a1)+str(b1)].append(str(t1) + str(t2))

prevs = ['0', '1', '2', '3']
# print(valids)
for i in range(0, len(a)):
	# valids = list()
	# for p in range(4):
	# 	for t in range(4):
	# 		if (p | t == a[i] and p & t == b[i]):
	# 			valids.append(p+t)
	newprevs = list()
	for i in valids[str(a[i])+str(b[i])]:
		for j in prevs:
			if j[-1] == i[0]:
				newprevs.append(str(j) + str(i[1]))
				# print(i, j)
				break
	prevs = newprevs

if (len(prevs) > 0):
	print('YES')
	print(' '.join(prevs[0]))
else:
	print('NO') 
