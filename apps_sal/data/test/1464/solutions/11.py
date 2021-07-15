n=int(input())
l=[]
for i in range(n):
	l+=[input()]
s="+".join(l)	
q="abcdefghijklmnopqrstuvwxyz"

for i in q:
	if i not in s:
		print(i)
		break
else:		
	for i in q:
		for j in q:
			if i+j not in s:
				print(i+j)
				return
