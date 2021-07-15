t=int(input())
for _ in range(t):
	n=int(input())
	a=input()
	ans=0
	for i in range(n):
		if a[i]=='A':
			count=0
			for j in range(i+1,n):
				if a[j]=='P':
					count+=1
				else:
					break
			ans=max(ans,count)
		else:
			continue
	print(ans)

