n,k = list(map(int,input().split()))
c = 0 
s = input()
st = 1
while st<n:
	flag = 0 
	sk = 0 
	for i in range(st,min(st+k,n)):
		if s[i]=='1':
			sk = i
			flag = 1
	if not flag :
		break
	c +=1
	st = sk+1
if flag :
	print(c)
else:
	print(-1)

