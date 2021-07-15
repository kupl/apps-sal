def help():
	n = int(input())
	arr = list(map(int,input().split(" ")))

	peak = [False]*n
	down = [False]*n
	for i in range(n):
		if(i==0):
			if(arr[0]<arr[1]):
				down[0]=True
			if(arr[0]>arr[1]):
				peak[i]=True
		elif(i==n-1):
			if(arr[n-1]<arr[n-2]):
				down[i]=True
			if(arr[n-1]>arr[n-2]):
				peak[i]=True
		else:
			if(arr[i-1]<arr[i] and arr[i]>arr[i+1]):
				peak[i]=True
			elif(arr[i-1]>arr[i] and arr[i]<arr[i+1]):
				down[i]=True
	series = []
	for i in range(n):
		if(peak[i]==True or down[i]==True):
			series.append(i)
	ans = 0
	for i in range(len(series)-1):
		ans += abs(series[i]-series[i+1])
	print(len(series))
	for i in range(len(series)):
		print(arr[series[i]],end=" ")
	print()

for _ in range(int(input())):
	help()

