n = int(input())
arr = list(map(int,input().split()))
marr= [(arr[2]-arr[0])/2,arr[2]-arr[1],arr[1]-arr[0]]
for m in marr:
	arr1=[]
	for x,y in enumerate(arr):
		arr1.append(y-m*(x+1))
	if len(set(arr1))==2:
		print("Yes")
		return
print("No")
