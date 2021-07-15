
n,x,y=list(map(int,input().split(" ")))
a=list(map(int,input().split(" ")))

for i in range(n):

	flg=True

	for j in range(max(0,i-x),i):
		if(a[j]<=a[i]):
			flg=False

	for j in range(i+1,min(n,i+y+1)):
		if(a[j]<=a[i]):
			flg=False

	if(flg):
		print(i+1)
		return

