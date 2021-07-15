import math

n,a,b = input().split()

n,a,b = int(n), int(a), int(b)

a-=1
b-=1

a=format(a, '010b')
b=format(b, '010b')

for i in range(len(a)):
	if (a[i]!=b[i]):
		if (len(a)-i==math.log(n,2)):
			print('Final!')
		else:
			print(len(a)-i)
		break
