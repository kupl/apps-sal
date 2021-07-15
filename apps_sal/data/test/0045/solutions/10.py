from math import sqrt

n , k = (int(i) for i in input().split())

def Provera (n, k):
	if (k * (k + 1)) // 2 > n:
		return True

if (Provera(n,k)):
	print (-1)
	return

for i in range(2, int(sqrt(n)) + 1):
	if (n % i == 0):
		NZD = n // i
		if not (Provera (i , k)):
			if (k * (k + 1)) // 2  == i:
				for j in range(1, k + 1):
					print (NZD * j,end = ' ')
				return
			if (k * (k + 1)) // 2  < i:
				for j in range(1, k):
					print (NZD  * j,end = ' ')
				print (n - NZD * ((k * (k - 1)) // 2))
				return
for i in range(int(sqrt(n)) + 1, 0, -1):
	if (n % i == 0):
		if not (Provera (n // i , k)):
			if (k * (k + 1)) // 2  ==  (n // i):
				for j in range(1, k + 1):
					print (i * j,end = ' ')
				return
			if (k * (k + 1)) // 2  < (n // i):
				for j in range(1, k):
					print (i  * j,end = ' ')
				print (n - i * ((k * (k - 1)) // 2))
				return
if (k * (k + 1)) // 2 == n:
	for i in range(1, k + 1):
		print (i, end = ' ')
else:
	for i in range(1, k):
		print (i, end = ' ')
	print (n - (k * (k - 1)) // 2)
