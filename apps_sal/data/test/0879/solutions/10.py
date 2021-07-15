n=int(input())
arr=list(map(int,input().split()))
res=[n]
while res[-1]!=arr[0]:
	res.append(arr[res[-1]-2])
res.sort()
for i in res:
	print(i,end=" ")
