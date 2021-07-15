n,k=list(map(int,input().split()))
dict1={}
for i in range(n):
	x=int(input())
	try:
		dict1[x]+=1
	except:
		KeyError
		dict1[x]=1
ans=0
flagcount=0
for i in list(dict1.keys()):
	ans+=((dict1[i])//2)*2
	if(dict1[i]%2!=0):
		flagcount+=1
if(n%2==0):
	ans+=(flagcount)//2
else:
	ans+=(flagcount)//2
	ans+=1
print(ans)


