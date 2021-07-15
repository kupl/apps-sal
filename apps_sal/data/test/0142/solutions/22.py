n,L=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
costPerLemon=[]
ans=12345678901234567890

for i in range(n):
	costPerLemon.append(c[i]/2**i)


size=n
money=0
while size>1:
	target=min(costPerLemon)
	i=costPerLemon.index(target)
	
	times=int(L/(2**i))
	money+=c[i]*times
	L-=(2**i)*times
	
	ans=min(ans,money+c[i])
	size=i
	while len(costPerLemon)>size:
		costPerLemon.pop(-1)
money+=L*c[0]
ans=min(ans,money)

print(ans)


