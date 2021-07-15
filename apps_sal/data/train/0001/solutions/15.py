def m():
	[x, y, k] = [int(i) for i in input().split()]
	d=min(x, y)
	x-=d
	y-=d
	k-=d
	
	if k-x-y<0:
		print(-1)
	else:
		x+=y
		if x%2 > 0 and k%2>0:
			print(d+k-1)
		elif x%2 >0:
			print(d+k-1)
		elif k%2>0:
			print(d+k-2)
		else:
			print(d+k)
			
		
			
	
n=int(input())
for i in range(n):
	m()
