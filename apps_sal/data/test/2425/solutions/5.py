from math import sqrt
q = int(input())
for _ in range(q):
	a = int(input())
	bi = format(a, 'b')
	if bi.count("0") == 0:
		for i in range(2, int(sqrt(a))+1):
			if a%i == 0:
				print(a//i)
				break
		else:
			print(1)
	else:
		print(pow(2, len(bi)) - 1)
