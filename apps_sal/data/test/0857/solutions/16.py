m, n = [int(i) for i in input().split()]
cons = input().split()
real = [i for i in input().split()]

ht = {}
for i in real:
	ht[i] = True

ans = []
for i in cons:
	if ht.get(i, None) == True:
		ans.append(i)

print(" ".join(ans))
