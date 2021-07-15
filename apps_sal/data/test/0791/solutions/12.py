n=input()
s=input()
i=1
if n=='1':
	print(1)
else:
	while s[i-1]=='1':
		i+=1
		if i>=len(s):
			break
	print(i)
