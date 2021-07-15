from math import sqrt
t=int(input())
for _ in range(t):
	n=int(input())
	ans=set()
	ans.add(0)
	root=int(sqrt(n))
	for x in range(1,root+1):
		ans.add(x)
		ans.add(n//x)
	print(len(ans))
	ans=sorted(ans)
	for x in ans:
		print(x,end=' ')
	print()
