s=input()
n=len(s)
l=[]
x=0
y=0
f=0
k=0
for i in range (26):
	l.append(0)
for i in range (n-25):
	for t in range (26):
		if s[i+t]=='?':
			y=y+1
		elif l[ord(s[i+t])-ord('A')]==0:
			l[ord(s[i+t])-ord('A')]=1
			y=y+1
		else:
			for j in range (26):
				l[j]=0
			y=0
		if y==26:
			f=1
			break
	if f==1:
		break
	for j in range (26):
		l[j]=0
	y=0
i=i+25
if f==0:
	print(-1)
else:
	for j in range(n):
		if j<(i-25) or (j>i):
			if s[j]=='?':
				print('A', end='')
			else:
				print(s[j], end='')
		else:
			if s[j]=='?':
				while l[k]!=0:
					k=k+1
				
				print(chr(k+ord('A')), end='')
				k=k+1
			else:
				print(s[j], end='')
print

	

