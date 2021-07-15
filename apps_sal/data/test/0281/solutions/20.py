a,b=list(map(int,input().split()))
fact=1
if(b-a<5):
	for i in range(a+1,b+1):
		fact*=i
	print(fact%10)
else:
	print(0)

