n=int(input())
a=input().split()
s=n*(n+1)//2
for i in range(n-1):
	s-=int(a[i])
print(s)

