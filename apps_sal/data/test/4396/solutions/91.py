N=int(input())
ans=0
for i in range(N):
	x,u=map(str, input().split())
	if u=="BTC":
		ans+=float(x)*380000
	else:
		ans+=float(x)
	#print(ans)

print(ans)
