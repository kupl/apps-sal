import sys
t=int(input())
for _ in range(t):
	n=int(input())
	l = list(map(int,sys.stdin.readline().split()))
	ans = 0
	for i in range(n):
		if l[i]==0:
			ans+=1
			l[i]=1
	if sum(l)==0:
		ans+=1
	print(ans)

