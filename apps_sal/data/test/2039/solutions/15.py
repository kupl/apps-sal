n = int(input())
a = list(map(int,input().split()))
c = 0
for i in range(1,n-1):
	if a[i-1]>a[i]<a[i+1]:
		c+=1
	elif a[i-1]<a[i]>a[i+1]:
		c+=1
print(c)

