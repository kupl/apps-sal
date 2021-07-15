import math
for nt in range(int(input())):
	n,k = map(int,input().split())
	s = input()
	ind = []
	for i in range(n):
		if s[i]=="1":
			ind.append(i)
	if len(ind)==0:
		print (math.ceil(n/(k+1)))
		continue
	count = ind[0]//(k+1)
	for i in range(1,len(ind)):
		count += max(0,math.ceil((ind[i]-ind[i-1]-2*k-1)/(k+1)))
	count += (n-ind[-1]-1)//(k+1)
	print (count)
