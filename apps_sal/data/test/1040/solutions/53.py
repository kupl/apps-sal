n=int(input())
s=input()
l=["0"]
for i in s:
	if l[-1]=="o":
		if l[-2]=="f" and i=="x":
			l.pop()
			l.pop()
		else:
			l.append(i)
	else:
		l.append(i)
print(len(l)-1)
