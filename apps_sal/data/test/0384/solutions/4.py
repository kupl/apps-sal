import re
n=int(input())
s=input()
l=re.findall('(B+)',s)
print(len(l))
for i in l:
	print(len(i),end=' ')

