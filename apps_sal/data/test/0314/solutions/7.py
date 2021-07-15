n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
days=0
stock=0
while(k>0 and days<n):
	stock+=l[days]
	k-=min(stock,8)
	stock-=min(stock,8)
	days+=1
if(k>0):
	print(-1)
else:
	print(days)
