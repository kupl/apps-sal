str_params = input()
[n, k]= [int(s) for s in str_params.split(' ')]
parts = (1+k)/2*k
if parts<=n:
	nod = n/parts
	while (nod%1!=0)|(parts%1!=0):
		if nod<parts:
			if nod%1!=0:
				nod = int(nod)
			else:
				nod = nod-1
			parts = n/nod
		else:
			if parts%1!=0:
				parts = int(parts)+1
			else:
				parts = parts+1
			nod = n/parts
	numbers = [nod*(x+1) for x in range(k)]
	numbers[k-1] = n-(1+k-1)/2*(k-1)*nod
	
	if numbers[0]==0:
		print(-1)
	else:
		print(' '.join(map(str,list(map(int, numbers)))))
else:
	print(-1)
	
"""while (sum(numbers)<n):
	

	33/5 = 6.6
	33/11 = 3
	
	33/6 = 5.5
	
	24/10 = 2.4
	
	
	
i = 1
while (sum(numbers)<n) & (i<k):
	while sum(numbers)<n:
		numbers = [numbers[x]*i for x in range(k)]
		print (i, numbers)
		i = i+1
print (numbers)
if sum(numbers)>n:
	print (-1)
if sum(numbers)==n:
	print (' '.join(map(str,numbers)))"""
	

