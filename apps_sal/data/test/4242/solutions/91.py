#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

a,b,k=input2()
MAX=max(a,b)
count=0
ans=0
for i in range(MAX,0,-1):
	if a%i==0 and b%i==0:
		count+=1
		if count==k:
			print(i)
			break
