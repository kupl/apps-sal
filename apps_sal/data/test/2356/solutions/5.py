

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	a=sorted(a)
	a=a[::-1]
	print(*a)
