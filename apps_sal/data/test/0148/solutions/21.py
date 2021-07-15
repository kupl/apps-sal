n,a,x,b,y = list(map(int,input().split()))
join = False
#print(min((x-a)%n, (b-y)%n))
for k in range(min((x-a)%n, (b-y)%n)+1):
	if a==b:
		join = True
	a+=1
	a%=n
	b-=1
	b%=n
if join:
	print('YES')
else:
	print('NO')

