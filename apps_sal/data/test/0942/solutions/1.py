import math

def __starting_point():

	n = int(input())
	arr = [int(x) for x  in input().split()]


	ans  = []
	d = {}
	c = {}
	b = [0]*n
	ind  = 0 
	for i in range(n) : 
		if arr[i] in list(d.keys()) : 
			if d[arr[i]]== 0 :
				ind+=1
				c[arr[i]]=ind
				b[i]=ind
				d[arr[i]]=n-arr[i]-1
			else :
				d[arr[i]]-=1
				b[i]=c[arr[i]]
		else : 
			ind+=1
			c[arr[i]]=ind
			b[i]=ind
			d[arr[i]]=n-arr[i]-1
	ans = True
	for i in d : 
		if d[i]!=0:
			ans =False
	if ans : 
		print ("Possible")
		print(*b)
	else : 
		print("Impossible")






__starting_point()
