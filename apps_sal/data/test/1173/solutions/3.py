def main():
	from collections import deque
	n=int(input())
	battle=n*(n-1)//2
	lis=[[] for i in range(battle)]
	num=[-1]*(n**2)
	cnt=-1
	for x in range(n**2):
		if x//n<x%n:
			cnt+=1
			num[x]=cnt
	for i in range(n):
		a=list(map(int,input().split()))
		for j in range(n-2):
			x=a[j]-1
			y=a[j+1]-1
			px=num[min(i*n+x,x*n+i)]
			py=num[min(i*n+y,y*n+i)]
			lis[px].append(py)
	node_in=[0]*(battle)
	for i in range(battle):
		for x in lis[i]:
			node_in[x]+=1
	zero=deque([])
	days=[10**9]*(battle)
	for i in range(battle):
		if node_in[i]==0:
			zero.append(i)
			days[i]=1
	while zero:
		r=zero.popleft()
		for x in lis[r]:
			node_in[x]-=1
			if node_in[x]==0:
				zero.append(x)
				days[x]=days[r]+1
	if 10**9 in days:
		print(-1)
	else:
		print(max(days))
def __starting_point():
	main()
__starting_point()
