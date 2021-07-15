n=int(input())
L=input().strip().split(' ')
x=0
for i in L:
	z=0
	for k in i:
		if ord(k)<95:
			z+=1
	x=max(x,z)
print(x)
