N=int(input())
SP=sorted([list(input().split())+[_+1] for _ in range(N)])
tempcity=SP[0][0]
ans=[]
tempans=[]
for i in range(N):
	#print(tempans)
	if tempcity == SP[i][0]:
		tempans.append([int(SP[i][1]),SP[i][2]])
	else:
		tempans=sorted(tempans, reverse=True)
		for h in range(len(tempans)):
			ans.append(tempans[h][1])
		tempans=[]
		tempcity=SP[i][0]
		tempans.append([int(SP[i][1]),SP[i][2]])
	if i==N-1:
		tempans=sorted(tempans, reverse=True)
		for h in range(len(tempans)):
			ans.append(tempans[h][1])
		
for g in range(N):print(ans[g])
