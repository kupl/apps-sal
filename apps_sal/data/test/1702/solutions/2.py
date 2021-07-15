def f(v, x, n):
	if v<0:
		return 0
	elif x<<1>n:
		return int( 500*(1-v/250))
	elif x<<2>n:
		return int(1000*(1-v/250))
	elif x<<3>n:
		return int(1500*(1-v/250))
	elif x<<4>n:
		return int(2000*(1-v/250))
	elif x<<5>n:
		return int(2500*(1-v/250))
	else:
		return int(3000*(1-v/250))

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
c=[sum(_[i]>=0 for _ in a) for i in range(5)]
ans=-1
for i in range(10000):
	p, q=0, 0
	for j in range(5):
		x, y=c[j], n
		if a[0][j]>a[1][j] and a[1][j]>=0:
			x+=i
		p+=f(a[0][j], x, n+i)
		q+=f(a[1][j], x, n+i)
	if p>q:
		ans=i
		break
print(ans)





# Made By Mostafa_Khaled

