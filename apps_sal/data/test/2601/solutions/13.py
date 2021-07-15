t=int(input())
for _ in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	s=set(arr)
	arr2=arr.copy()
	arr2.sort(reverse=True)
	if(len(s)==n and arr2==arr):
		print("NO")
	else:
		print("YES")
