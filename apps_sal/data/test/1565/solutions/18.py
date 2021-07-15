n=int(input())
s=input()
x=n//2
ans=int(s)
if(s[x]!='0'):
	ans=min(ans,int(s[:x])+int(s[x:]))
for i in range(x+1,n):
	if(s[i]!='0'):
		ans=min(ans,int(s[:i])+int(s[i:]))
		break
for i in range(x-1,0,-1):
	if(s[i]!='0'):
	#	print(i,s[:i],s[i:])
		ans=min(ans,int(s[:i])+int(s[i:]))
		break
print(ans)
