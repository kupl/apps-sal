a = list(map(int, input().split()))
n = a[0]
q = a[1]

ans = []
starte = 0

if (n % 2 == 1):
	starto = (n**2)//2 + 1
else:
	starto = (n**2)//2

for i in range(q):
	a = list(map(int, input().split()))
	x = a[0]
	y = a[1]
	
	line = x
	cell = y

	if(n % 2 == 1):
		if (line % 2 == 0):
			if((x+y) % 2 == 1):
				t = (line//2)*(n//2) + (line//2-1)*(n//2+1) + starto + (cell // 2) + 1
			else:
				t = (line//2-1)*(n//2) + (line//2)*(n//2+1) + starte + (cell // 2)
		else:
			if((x+y) % 2 == 1):
				t = (line//2)*(n//2+1) + (line//2)*(n//2) + starto + (cell // 2)
			else:
				t = (line//2)*(n//2+1) + (line//2)*(n//2) + starte + (cell // 2) + 1
	else:
		if (line % 2 == 0):
			if((x+y) % 2 == 0):
				t = (line-1)*(n//2) + starte + (cell // 2)
			else:
				t = (line-1)*(n//2) + starto + ((cell // 2) + 1)
		else:
			if((x+y) % 2 == 1):
				t = (line-1)*(n//2) + starto + (cell // 2)
			else:
				t = (line-1)*(n//2) + starte + (cell // 2) + 1
	
	ans.append(t)
	
for i in range(q):
	print(ans[i])
				

