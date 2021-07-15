a,b = list(map(int,input().split()))
times = 0
while (a <= b) :  
	a = a * 3
	b = b * 2
	times += 1
print(times)

