n=int(input())
arr=list(map(int,input().split()))
arr.sort()
if(arr[-1]>=arr[-2]+arr[-3]):
	print("NO")
else:
	print("YES")
	ansarr=[arr[-3],arr[-1],arr[-2]]
	for i in range(n-4,-1,-1):
		ansarr.append(arr[i])
	print(*ansarr)
