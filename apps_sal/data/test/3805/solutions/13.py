l=input()
l=list(l)

p=[]

for i in l:
	if len(p)==0:
		p.append(i)
	elif p[-1]==i:
		p.pop()
	else:
		p.append(i)
	#print(p)
if len(p)==0:
	print('Yes')
else:
	print('No')
