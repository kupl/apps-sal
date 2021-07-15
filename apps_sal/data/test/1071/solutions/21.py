from math import ceil

a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = int(input())

cups_space = ceil(sum(a)/5)
medals_space = ceil(sum(b)/10)

if cups_space+medals_space <= n:
	print('YES')
else:
	print('NO')

