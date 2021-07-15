n=int(input())
a=[]
for i in range(n):
	a.append(tuple(map(int,input().split())))
a.sort(key=lambda x:x[1])
cnt=0;cur=-10
i=0
while i<n:
	if cur<a[i][0]:
		cur=a[i][1]
		cnt+=1
	i+=1
print(cnt)

