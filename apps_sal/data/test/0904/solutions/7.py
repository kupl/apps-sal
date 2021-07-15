n=int(input())
a=input().split()
ans=0
for i in a:
	tot=0
	for j in i:
		if(j.isupper()):tot+=1
	ans=max(ans,tot)
print(ans)

