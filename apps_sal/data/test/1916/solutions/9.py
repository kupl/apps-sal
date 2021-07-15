a,b=map(int,input().split())
r1=list(map(int,input().split()))
r2=list(map(int,input().split()))
for target in range(2**9):
	ans=0
	g = True
	for i in range(a):
		f = False
		for j in range(b):
			t = r1[i] & r2[j]
			if t & target == t:
				f = True
				break
		if not f:
			g = False
			break
	if g:
		print(target)
		return
