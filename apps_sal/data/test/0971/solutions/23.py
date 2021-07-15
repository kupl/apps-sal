s=input().split()
n=int(s[0])
b=int(s[1])
d=int(s[2])
k=input().split()
a=0
p=0
for i in k:
	if int(i)<=b:
		p+=int(i)
		if p>d:
			a+=1
			p=0
print(a)

