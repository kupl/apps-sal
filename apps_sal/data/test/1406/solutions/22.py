import math 
n,k,d = list(map(int,input().split()))
# if math.log(n)>d*math.log(k): chadar%
if n>k**d:
	print(-1)
else:
	# no pgh shit 
	t = 1
	for i in range(d):
		li = []
		for j in range(n):
			li.append((j//t)%k+1)
		print(*li)
		t*=k

