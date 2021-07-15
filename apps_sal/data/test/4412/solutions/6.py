q = int(input())
for w in range(q):
	n = int(input())
	arr = list(map(int,input().split()))
	arr = list(set(arr))
	arr.sort(reverse=True)
	n = len(arr)
	ans=0
	for i in range(n):
		ans = max(ans,arr[i])
		for j in range(i+1,n):
			if arr[i]%arr[j]!=0:
				ans = max(ans,arr[i]+arr[j])
				if j+1<n and ans>= arr[i]+arr[j+1]+arr[j]:
					break
				for k in range(j+1,n):
					if ans>=arr[i]+arr[j]+arr[k]:
							break
					if arr[j]%arr[k]!=0 and arr[i]%arr[k]!=0:
						ans = max(ans,arr[i]+arr[j]+arr[k])
	print(ans)


