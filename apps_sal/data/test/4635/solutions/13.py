k = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(k):
	m , n = list(map(int,input().split()))
	if n > m:
		print(s[:m])
	else:
		print(s[:n]*(m//n) + s[:m%n])

