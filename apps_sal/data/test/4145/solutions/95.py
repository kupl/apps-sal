X=int(input())
flag=0

if X==2 or X==3:
	flag=1

while flag==0:
	for k in range(2,int(X**0.5)+1):
		if k==int(X**0.5) and X%k!=0:
			flag=1
		
		if k>2 and k%2==0:
			continue
		elif k>3 and k%3==0:
			continue
		elif X%k==0:
			break
	
	if flag==0:X=X+1	
		
print(X)

