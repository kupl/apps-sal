n, ls = int(input()), sorted(list(map(int, input().split())))
ls1, ls2 = [],[]
for i in range(n):
	if i & 1: ls1.append(ls[i])
	else: ls2.append(ls[i])
tls = list(reversed(ls2))+ls1
print(" ".join([str(l) for l in tls]))
