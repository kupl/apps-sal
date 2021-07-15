n = int(input())
a = [0]
b = [int(i) for i in input().split()]
a+=b
ans = 0
for i in range(1,n+1):
	if(a[i-1]<a[i]):
		ans+=(a[i]-a[i-1])*(n-a[i]+1)
	else:
		ans+=a[i]*(a[i-1]-a[i])
print(ans)

