x,y,m = list(map(int,input().split()))
if(x > y):
	x,y = y,x
if(y >= m):
	print('0')
elif(x+y <= x):
	print('-1')
else:
	ans = (y-x+y-1)//y
	x += y*ans
	while(x < m):
		x,y = x+y,x
		ans += 1
	print(ans)


