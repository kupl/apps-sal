t=int(input())
for tt in range(t):
	x=int(input())
	temp=x
	cc=0
	while temp>0:
		start=0
		end=temp
		ans=0
		while start<=end:
			mid=(start)+(end-start)//2
			xx=mid*((3*mid)+1)//2
			if xx<=temp:
				start=mid+1
				ans=max(ans,mid)
			else:
				end=mid-1
		if ans==0:
			break
		temp-=(ans*((3*ans)+1))//2
		cc+=1
	print(cc)
