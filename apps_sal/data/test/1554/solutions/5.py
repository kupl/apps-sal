n = int(input())
li = list(map(int,input().split()))
s=set()
ans=[]
l=0
r=-1
for i in range(n):
	if li[i] in s:
		ans.append([l+1,i+1])
		s = set()
		l = i+1
		r=1
	else:
		s.add(li[i])
if r==-1:
	print(-1)
else:
	print(len(ans))
	ans[len(ans)-1][1]=n
	for i in ans:
		print(*i)
