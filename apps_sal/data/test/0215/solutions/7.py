import re
n=int(input())
s=input()
ans=0
for c in re.split('[A-Z]',s):
	if len(c)>0:
		ans=max(ans,len(set(c)))

print(ans)

