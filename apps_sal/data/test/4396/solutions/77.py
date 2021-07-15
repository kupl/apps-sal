N = int(input())

JPY = 0
BTC = 0
for i in range(N):
	a, b = input().split()
	if b == 'JPY':
		JPY += float(a)
	else:
		BTC += float(a)
print(JPY + 380000.0 * BTC)
