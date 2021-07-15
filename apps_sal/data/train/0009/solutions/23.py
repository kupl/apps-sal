for i in range(int(input())):
	ip=list(map(int,input()))
	ones=[]
	tot=0
	for i in ip:
		if i==1:
			tot+=1
		else:
			ones.append(tot)
			tot=0
	if tot:ones.append(tot)
	ones.sort(reverse=True)
	ans=0
	for i in range(0,len(ones),2):
		ans+=ones[i]
	print(ans)
