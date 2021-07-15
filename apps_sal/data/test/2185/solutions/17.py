q = int(input())
for i in range(q):
	n = int(input())
	mas1 = list(map(int, input().split()))
	mas2 = list(map(int, input().split()))
	flag = 0
	al = True
	p = 0
	for j in range(n):
		if mas1[j] != mas2[j]:
			if flag == 0:
				flag = 1
				p = mas1[j] - mas2[j]
				if p > 0:
					al = False
					break
			elif flag == 1:
				if p != mas1[j] - mas2[j]:
					al = False
					break
			else:
				al = False
				break
		else:
			if flag == 1:
				flag = 2
	if al:
		print("YES")
	else:
		print ("NO")

