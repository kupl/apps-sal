t=int(input())
for ij in range(0,t):
	l=list(map(int,input().split()))
	l=sorted(l)
	if l[2]>l[1]+l[0]:
		print(l[1]+l[0])
	else:
		print(sum(l)//2)
