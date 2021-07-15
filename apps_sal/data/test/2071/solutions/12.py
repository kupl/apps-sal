n=int(input())
x=map(int,input().split())
a=[[],[]]
k=0
for i in x:
	a[0].append(i)
	k+=i
x=map(int,input().split())
for i in x:
	a[1].append(i)
	k+=i
sum=[[0],[0]]
for i in range(2):
	for j in range(1,n+1):
		sum[i].append(sum[i][j-1]+a[i][n-j])
sum2=[[0],[0]]
for i in range(2):
	for j in range(1,n+1):
		sum2[i].append(sum2[i][j-1]+sum[i][j])
sum3=[[0],[0]]
for i in range(2):
	for j in range(1,n+1):
		sum3[i].append(sum3[i][j-1]+a[i][n-j]*j)
ans=0
now=0
for i in range(n):
	pos=n-i
	line=i%2
	ans=max(ans,now+sum[0][pos]*i*2+sum[1][pos]*i*2+sum2[line][pos]+sum3[1-line][pos]+sum[1-line][pos]*(n-i))
	now+=(2*i+1)*a[line][i]+(2*i+2)*a[1-line][i]
print(ans-k)
