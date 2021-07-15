for nt in range(int(input())):
	s=input()
	n=len(s)
	arr=[]
	c=1
	prev=s[0]
	for i in range(1,n):
		if s[i]==prev:
			c+=1
		else:
			arr.append((prev,c))
			prev=s[i]
			c=1
	arr.append((prev,c))
	# print (arr)
	m=10**9
	for i in range(len(arr)-2):
		if arr[i][0]!=arr[i+1][0] and arr[i][0]!=arr[i+2][0]:
			m=min(m,arr[i+1][1]+2)
	if m==10**9:
		print (0)
	else:
		print (m)
