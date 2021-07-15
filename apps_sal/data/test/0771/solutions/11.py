l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
c = [0 for i in range(l1[2])]

for i in l2:
	c[i%l1[2]]+=1
a = []
I=-1
for i in range(l1[2]):
	if c[i]>=l1[1]:
		I=i
		break
if I>=0:
	print('Yes')
	i = 0
	j = 0
	while j<l1[1]:
		if l2[i]%l1[2]==I:
			a.append(str(l2[i]))
			j+=1
		i+=1
	print(" ".join(a))
else:
	print('No')
    

