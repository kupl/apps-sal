n = int(input())
arr = input().split()
if(n%2 == 1):
	for i in range(n):
		if(i%2 == 1):
			print(arr[i], end=" ")
		else:
			print(arr[(n-1)-i], end=" ")
else:
	for i in range(n//2):
		if(i%2 == 1):
			print(arr[i], end=" ")
		else:
			print(arr[(n-1)-i], end=" ")
	for i in range(n//2,n):
		if(i%2 == 0):
			print(arr[i], end=" ")
		else:
			print(arr[(n-1)-i], end=" ")
