def compare(a,b):
	nonlocal good,replacements
	if(a==b):
		return 1
	elif(b=='?' and (a in good)):
		return 1
	elif(b=='*' and (a not in good)):
		if(replacements<0):
			return 0
		else:
			return replacements+10
	elif(b=='*' and (a in good)):
		return 2
	else:
		return 0

g = input()
good={}
for val in g:
	good[val]=1
patt = input()
n=int(input())
for i in range(n):
	q=input()
	replacements = len(q)-len(patt)+1
	it=0
	c=0
	while(c<len(q) and it<len(patt)):
		result=compare(q[c],patt[it])
		if(result==2):
			it+=1
		elif(result==1):
			it+=1
			c+=1
		elif(result>9):
			if(replacements==0):
				it+=1
			else:
				c+=1
				replacements-=1
		else:
			break
	if(it<len(patt)):
		if(patt[it]=='*'):
			it+=1
	if(c==len(q) and it==len(patt)):
		print("YES")
	else:
		print("NO")

