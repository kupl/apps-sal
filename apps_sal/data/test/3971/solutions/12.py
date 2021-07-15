a=[0 for i in range(100010)]
f=[0 for i in range(100010)]
ans=0
n=int(input())
L=input().split()
for i in range(n):
	a[int(L[i])]+=1
for i in range(1,100001):
	f[i]=f[i-2]+i*a[i]
	ans=max(ans,f[i])
	f[i]=max(f[i],f[i-1])
print(ans)
return

