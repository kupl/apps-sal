s=input()
a,b=0,0
for i in range(len(s)):
	if(s[i]=='-'):
		a=a-1
		if a<b:
			b=a
	else:
		a=a+1
a=-b
ans=a
for i in range(len(s)):
	if(s[i]=='-'):
		a=a-1 
	else:
		a=a+1
	if a>ans:ans=a
print(ans)
