n, k = input().split(' ')
n = int(n)
k = int(k)
d = input().split(' ')
i = 0

while True:
	i += 1
	p = int((i) * (i+1) / 2)
	if k <= p :
		print(d[k-(p-i)-1])
		break
