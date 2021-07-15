q = int(input())
for w in range(q):
	n = int(input())
	arr = list(map(int,input().split()))
	arr = list(set(arr))
	arr.sort(reverse=True)
	n = len(arr)
	ansarr = [-1 for i in range(n)]
	maxans = 0
	for i in range(n):
		currans = arr[i]
		for j in range(i+1,min(i+171,n)):
			if arr[i]%arr[j]!=0:
				currans = max(currans,arr[i]+arr[j])
				if j+1<n and arr[i]+arr[j]+arr[j+1]<=maxans:
					break
				for k in range(j+1,min(j+171,n)):
					if arr[j]%arr[k]!=0 and arr[i]%arr[k]!=0:
						currans = max(currans,arr[i]+arr[j]+arr[k])
						if currans<=maxans:
							break
		ansarr[i]=currans
		maxans = max(maxans,currans)
	print(max(ansarr))
