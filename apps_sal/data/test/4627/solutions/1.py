q = int(input())
for i in range(q):
	n = int(input())
	l = list(map(int,input().split()))
	l.sort()
	kol = False
	for i in range(1,n):
		if l[i] == l[i-1] + 1:
			kol =True
			break
	par = 0
	npar = 0
	for i in l:
		if i%2 == 0:
			par += 1
		else:
			npar += 1
	if not kol:
		if par%2 == 0 and npar%2 == 0:
			print("YES")
		else:
			print("NO")
	else:
		if par%2 == 0 and npar%2 == 0:
			print("YES")
		elif par%2 == 1 and npar%2 == 1:
			print("YES")
		else:
			print("NO")
