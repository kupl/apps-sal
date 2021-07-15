def sum(a):
	s=0
	while a:
		s=s+a%10
		a=a//10
	return s
x=int(input())
temp=19
while x>1:
	temp=temp+9
	if sum(temp)==10:
		x=x-1
print (temp)
