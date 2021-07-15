for _ in range(int(input())):
	n=int(input())
	s=input()
	curr=None
	ans=0
	for i in s:
		if i=="A":
			curr=0
		elif curr!=None:
			curr+=1
			ans=max(ans,curr)
	print(ans)
