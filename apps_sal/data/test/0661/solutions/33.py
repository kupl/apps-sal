m,k=map(int,input().split())
if k>=2**m or m==k==1:
	print(-1)
elif m==1:
	print("1 1 0 0")
else:
	l=list(range(k))+list(range(k+1,2**m))
	print(*(l+[k]+l[::-1]+[k]))
