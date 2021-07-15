n = int(input())
ans = []
for i in range(n):
	mas = [int(x) for x in input().split()]
	tr = True
	for x in mas:
		if x == 1 or x == 3:
			tr = False
			break
	if tr:
		ans.append(i + 1)
		
print(len(ans))
ans = [str(x) for x in ans]
print(' '.join(ans))
