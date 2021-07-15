n=int(input())
s=sorted(map(int,input().split()))
ans=[]
i=0;j=n-1
for _ in range(n):
	if _%2==0:ans.append(s[j]);j-=1
	else:ans.append(s[i]);i+=1
res=0
for i in range(1,n-1):res+=ans[i-1]>ans[i]<ans[i+1]
print(res)
print(*ans)

