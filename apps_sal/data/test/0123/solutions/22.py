n,k = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
if(k!=1):
	print('Yes')
	return
for i in range(n):
	if(l1[i]==0):
		l1[i]=l2[0]
		break
ok = True
for i in range(n-1):
	if(l1[i+1]<l1[i]):
		ok = False
		break
if(ok==True):
	print('No')
else:
	print('Yes')
