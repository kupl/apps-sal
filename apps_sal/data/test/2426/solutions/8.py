import math
t=int(input())
for tt in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	flag=False
	odd=[]
	for i in range(len(arr)):
		if arr[i]%2==0:
			print(1)
			print(i+1)
			flag=True
			break
		else:
			odd.append(i+1)
			if  len(odd)%2==0:
				break
	if not flag:
		if len(odd)%2==1:
			print(-1)
			continue
		print(len(odd))
		for i in odd:
			print(i,end=" ")
		print()

