import sys

n=int(sys.stdin.readline())

m=[int(x) for x in sys.stdin.readline().split()]

ans=0

arr=[0]*n

for i in range(n):
	
	floors=m[i]
		
	tmp=[0]*n
	tmp[i]=m[i]

	prev=m[i]
	for j in range(i-1,-1,-1):
		num=min(prev,m[j])
		floors+=num
		tmp[j]=num
		prev=num

	p2=m[i]
	for k in range(i+1,n):
		n2=min(p2,m[k])
		floors+=n2
		tmp[k]=n2
		p2=n2

	if(floors>ans):
		ans=floors
		for g in range(n):
			arr[g]=tmp[g]

for p in range(n):
	print(arr[p],end=" ")
print()

