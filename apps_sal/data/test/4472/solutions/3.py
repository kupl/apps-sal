n = int(input().strip())
a = input().strip()
b = input().strip()
ans = 0
v = n//2
for i in range(v):
	j = n-i-1
	if a[i]==b[i]:
		if a[j]!=b[j]:
			ans+=1
	elif a[i]==b[j]:
		if a[j]!=b[i]:
			ans+=1
	elif a[j]==b[j]:
		if a[i]!=b[i]:
			ans+=1
	elif a[j]==b[i]:
		if a[i]!=b[j]:
			ans+=1
	elif a[i]==a[j]:
		if b[i]!=b[j]:
			ans+=2
	elif b[i]==b[j]:
		if a[i]!=a[j]:
			ans+=1
	else:
		ans+=2
if n&1:
	i = (n)//2
	if a[i]!=b[i]:
		ans+=1
print(ans)
