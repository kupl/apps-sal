n,r=list(map(int,input().split()))
a=[list(map(int,input().split())) for i in range(n)]
pos = []
neg = []
ans=0
for x in a:
	if x[1]>0:
		pos.append(x)
	else:
		neg.append(x)
pos.sort(key=lambda k: k[0])
flag=True
for x in pos:
	if r>=x[0]:
		r+=x[1]
		ans+=1

neg.sort(key=lambda i: i[0]+i[1],reverse=True)
arr=[0]*(r+1)
for i in range(len(neg)):
	for j in range(neg[i][0],r+1):
		if j+neg[i][1]>=0:
			arr[j+neg[i][1]]=max(arr[j+neg[i][1]],arr[j]+1)
ans+=max(arr)
print(ans)

