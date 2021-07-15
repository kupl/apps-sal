n=int(input())
a=[0]*n
for i in range(n-1):
	for j in input().split():
		a[int(j)-1]+=1
l=a.count(1)
print((l*2**(n-l+1)+(n-l)*2**(n-l))%1000000007)
