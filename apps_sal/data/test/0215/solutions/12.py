import re
n=int(input())
s=input()
a=re.split('[A-Z]+',s)
ans=0
for i in a:
	ans=max(ans,len(set(i)))
print(ans)
