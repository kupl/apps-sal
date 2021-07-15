

for _ in range(int(input())):
	nkl = list(map(int,input().split()))
	n = nkl[0]
	k = nkl[1]
	l = nkl[2]
	d = list(map(int,input().split()))
	flag=1
	count=0
	leez = 0
	for i in range(n):
		if(d[i]>l):
			flag=0
			break
		else:
			if(l-d[i]>=k):
				count=0
				continue
			count+=1
			if(count==1):
				leez = l-d[i]
				continue
			leez = min(leez-1,l-d[i])
			if(leez>=0):
				continue
			if(-leez<=l-d[i]):
				continue
			else:
				flag=0
				break
	if(flag==1):
		print("Yes")
	else:
		print("No")

	



