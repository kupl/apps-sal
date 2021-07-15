n=int(input())
l=list(map(int,input().split()))
i = 0
while i < n - i - 1:
	if i % 2 == 0:
		l[i],l[n-i-1]=l[n-i-1],l[i]
	i+=1
for i in range(n):
	print(l[i],end=' ')
