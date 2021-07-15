s=input()
newst=[]

curr='a'

for k in s:
	if curr>=k and curr<='z':
		newst.append(curr)
		curr=chr(ord(curr)+1)
	else:
		newst.append(k)
if curr>'z':
	for k in newst:
		print(k,end='')
	print()
else:
	print(-1)
