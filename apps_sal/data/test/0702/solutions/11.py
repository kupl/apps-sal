import math
from decimal import Decimal
def na():
	n = int(input())
	b = [int(x) for x in input().split()]
	return n,b


def nab():
	n = int(input())
	b = [int(x) for x in input().split()]
	c = [int(x) for x in input().split()]
	return n,b,c


def dv():
	n, m = list(map(int, input().split()))
	return n,m


def dva():
	n, m = list(map(int, input().split()))
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	return n,m,b


def nm():
	n = int(input())
	b = [int(x) for x in input().split()]
	m = int(input())
	c = [int(x) for x in input().split()]
	return n,b,m,c


def dvs():
	n = int(input())
	m = int(input())
	return n, m


n = int(input())
a = []
for i in range(n):
	s = input()
	s = list(s)
	a.append(s)
for i in range(1, n - 1):
	for j in range(1, n - 1):
		if a[i][j] == '.' and a[i][j + 1] == '.' and a[i][j - 1] == '.' and a[i - 1][j] == '.' and a[i + 1][j] == '.':
			a[i][j], a[i][j + 1], a[i][j - 1], a[i - 1][j], a[i + 1][j] = '#', '#', '#', '#', '#'
f = True
for i in a:
	for j in i:
		if j == '.':
			f = False
if f:
	print('YES')
else:
	print('NO')

