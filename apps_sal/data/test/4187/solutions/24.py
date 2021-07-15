n=int(input())
arr=list(map(int,input().split()))
arr.extend(arr)
maxi=0
cur=0
for i in range(len(arr)):
	if arr[i]==1:
		cur+=1
	else:
		if cur>maxi:
			maxi=cur
		cur=0
print(maxi)
