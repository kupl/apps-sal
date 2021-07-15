n=int(input())
L=[int(x) for x in input().split()]
L.sort(reverse=True)
i=0
while i<n-1:
	if L[i]-1==L[i+1]:
		L[i]-=1
		i+=1
	elif L[i]==L[i+1]:
		i+=1
	i+=1
val=[]
i=0
while i<n-1:
	if L[i]==L[i+1]:
		val.append(L[i])
		i+=1
	i+=1
area=0
n=len(val)
i=0
while i<n-1:
	area+=val[i]*val[i+1]
	i+=2
print(area)

