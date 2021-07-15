n=int(input())
a=int(input())
b=int(input())
l=u=0
ans=1
m=n
if 2*a+b==n:
	print(2)
	return
while l<4 or u<2:
	if m>=a and m>=b:
		if u<2 and l<4:
			if a>=b:
				m-=a
				l+=1
			else:
				m-=b
				u+=1
		elif l<4:
			m-=a
			l+=1
		else:
			m-=b
			u+=1
	else:
		if m<a and m>=b and u<2:
			m-=b
			u+=1
		elif m>=a and m<b and l<4:
			m-=a
			l+=1
		else:
			ans+=1
			m=n
print(ans)
