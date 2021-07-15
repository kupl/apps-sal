n=int(input())
l=list(map(int,input().strip().split()))
min1=1000000000000
index=11
for i in range(n):
	if l[i]<min1:
		min1=l[i]
		index=i
if n==1:
	print(-1)
elif n==2:
	if l[0]==l[1]:
		print(-1)
	else:
		print(1)
		print(index+1)
else:
	print(1)
	print(index+1)

