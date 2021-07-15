max = -float('inf')
cur = []

def candies(n, arr):
	nonlocal cur, max
	if sum(arr) == n:
		if len(arr) > max or (len(arr) == max and sum(arr) > sum(cur)):
			max = len(arr)	
			cur = arr[:]				
		return 0 

	if sum(arr) > n:
		arr.pop()
		if len(arr) > max or (len(arr) == max and sum(arr) > sum(cur)):		
			max = len(arr)
			cur = arr[:]				
		return 0

	for i in range(1, n+1):
		if i not in arr:
			arr.append(i)			
			if candies(n, arr) == 0:	
				break
			if i in arr: arr.remove(i);
	#print(cur)
	return 1
		

n = int(input())


candies(n, [])
print(max)
for each in cur:
	print(each, end=" ") 


