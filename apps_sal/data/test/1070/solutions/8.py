t,m = map(int,input().split())
arr = list(map(int,input().split()))

counter = 0
cache = 0
maxi = 0
for i in range(t):
	if(i==0):
		
		cache = arr[i]
		counter = counter+1
	else:
		if(cache!=arr[i]):
			counter= counter+1
			cache = arr[i]
			
		else:
			counter=1
	if(maxi<counter):
				maxi=counter

print(maxi)
