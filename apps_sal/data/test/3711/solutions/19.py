a,b,k = list(map(int,input().split()))
if a+b-2<k:
	print(-1)
	return
k+=2
if a>b:
	a,b=b,a

i = 1
maxi = -1
while (i*i<=a):

	y=min(i,k-1)
	val1 = (a//y)*(b//(k-y))
	if maxi<val1:
		maxi = val1

	j = min(a//i,k-1)
	val2 = (a//j)*(b//(k-j))
	if maxi<val2:
		maxi=val2
	i+=1
print(maxi)

