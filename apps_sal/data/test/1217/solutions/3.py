n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
resb = dict()
sa = sorted(a)
sb = sorted(b)
i = 0
j = 0
while j < len(sb):
	while i < len(sa) and sa[i] <= sb[j]:
		i += 1
	resb[sb[j]] = i
	j += 1
for i in b:
	print(resb[i], end=' ')

