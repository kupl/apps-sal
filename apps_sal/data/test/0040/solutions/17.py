n=int(input())
l1=[]
l2=[]
for i in range(n):
	a,b=map(int,input().split())
	l1.append(a)
	l2.append(b)
rc = False
for i in range(n):
	if(l1[i]!=l2[i]):
		rc=True
		break
if(rc==True):
	print("rated")
	return
tot = 0
for i in range(1,n):
	if(l2[i]<=l2[i-1]):
		tot+=1
if(tot==n-1):
	print("maybe")
	return
print("unrated")
