#NOOOOOOO!

s=list( input() )
l=len(s)
ln = []

if(l<2):
	ln=s
else:
	ln= s[0:2]
	
j=2	
for i in range(2,l):
	if s[i]!=ln[j-1] or s[i]!=ln[j-2]: #not the third consecutive
		if ln[j-1]!=ln[j-2] or i==l-1 or s[i]!=s[i+1]: #not two couples
			ln.append(s[i])
			j+=1
			
print(''.join(ln))



