t = int(input())
for _ in range(t):
	n = int(input())
	n += 1
	res = 0
	for i in range(60,-1,-1):
		temp = 1<<i 
		if temp <= n:
			temp1 = n//temp 
			if n%temp != 0:
				temp1 += 1 
			res += temp1 - 1 
	print(res)
