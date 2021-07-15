n=int(input())
ans=0
if(n<4):
	print('0')
	return
for i in range(2,(n//2)+1):
	k=n//i;
	ans+=(k*(k+1))//2-1
print(4*ans)
