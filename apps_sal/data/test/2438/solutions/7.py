def comp(a):
	if a=="A":
		return "B"
	else:
		return "A"

n=int(input())
s=input()
ans=(n*(n-1))//2
groups=[0]
prev=s[0]
for i in range(1,n):
	if s[i]!=prev:
		groups.append(i)
		prev=s[i]
for i in range(0,len(groups)-2):
	ans -= (groups[i+2]-groups[i]-1)
if len(groups)>1:
	ans -= (n-groups[-2]-1)
print (ans)
