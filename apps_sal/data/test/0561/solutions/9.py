def isProgression():
	nonlocal N,A,d,error
	ans = True
	for i in range(N-1):
		if(d!=A[i+1]-A[i]):
			ans = False
			error+=1
	return ans


N = int(input())
A = list(int(i) for i in input().split())
error = 0
A.sort()
d = (A[N-1]-A[0])//N
res = isProgression()
if(error==N-1 and N!=1 and (A[N-1]-A[0])%(N-1)==0):
	d = (A[N-1]-A[0])//(N-1)
	error = 0
	res = isProgression()
	
if(N==1):
	print(-1)
elif(N==2 and (A[0]+A[1])%2==0 and A[0]!=A[1]):
	print(3)
	d = A[1]-A[0]
	print(A[0]-d, (A[0]+A[1])//2, A[1]+d)
elif(res==True and d!=0):
	print(2)
	print(A[0]-d,A[N-1]+d)
elif(res==True):
	print(1)
	print(A[0])
elif(error>1):
	print(0)
else:
	for i in range(N-1):
		if(d!=A[i+1]-A[i]):
			if(A[i+1]-A[i]<d):
				print(0)
			elif(A[i+1]-A[i]==2*d):
				print(1)
				print((A[i]+A[i+1])//2)
			else:
				print(0)
			break

