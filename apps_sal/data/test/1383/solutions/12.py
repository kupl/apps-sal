n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
ans=[]
for i in range(n):
	if b[-1]<a[i]:
		ans.append(b[-1]-a[i]+m)
		#ans.append(b[-1]-a[i]+m+m)
	else:
		ans.append(b[-1]-a[i])
		#ans.append(b[-1]-a[i]+m)
ans=list(set(ans))
ans.sort()
for i in ans:
	temp=[]
	for j in range(n):
		temp.append((a[j]+i)%m)
	if sorted(temp)==b:
		print (i)
		return
print(1/0)
	


