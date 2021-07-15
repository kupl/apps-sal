n, s = list(map(int, input().split()))
m = -1
for i in range(n):
	x, y = list(map(int, input().split()))
	csum = (s-x)*100 - y
	if  csum <=s*100 and csum >=0 and csum%100 > m:
		m = csum%100
print(m)

